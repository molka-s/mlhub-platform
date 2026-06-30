from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.experiment import Experiment
from app.ml.trainer import train_model

router = APIRouter(prefix="/training", tags=["Training"])

@router.post("/run/{experiment_id}")
def run_training(experiment_id: int, db: Session = Depends(get_db)):
    experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not experiment:
        raise HTTPException(status_code=404, detail="Expérience introuvable")

    # Récupère les paramètres définis dans l'expérience (ou valeurs par défaut)
    params = experiment.parameters or {}
    n_estimators = params.get("n_estimators", 100)
    max_depth = params.get("max_depth", 5)

    # Met à jour le statut
    experiment.status = "running"
    db.commit()

    try:
        result = train_model(
            n_estimators=n_estimators,
            max_depth=max_depth,
            experiment_name=experiment.name
        )

        # Sauvegarde les résultats dans la base
        experiment.status = "done"
        experiment.metrics = {
            "accuracy": result["accuracy"],
            "f1_score": result["f1_score"],
            "mlflow_run_id": result["run_id"]
        }
        db.commit()
        db.refresh(experiment)

        return {
            "message": "Entraînement terminé",
            "experiment_id": experiment.id,
            "status": experiment.status,
            "metrics": experiment.metrics
        }

    except Exception as e:
        experiment.status = "failed"
        db.commit()
        raise HTTPException(status_code=500, detail=f"Erreur d'entraînement: {str(e)}")