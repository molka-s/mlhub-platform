from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.experiment import Experiment
from app.schemas.experiment import ExperimentCreate, ExperimentUpdate, ExperimentResponse

router = APIRouter(prefix="/experiments", tags=["Experiments"])

@router.post("/", response_model=ExperimentResponse, status_code=201)
def create_experiment(data: ExperimentCreate, db: Session = Depends(get_db)):
    experiment = Experiment(**data.model_dump(), owner_id=1)  # owner_id temporaire
    db.add(experiment)
    db.commit()
    db.refresh(experiment)
    return experiment

@router.get("/", response_model=List[ExperimentResponse])
def get_experiments(db: Session = Depends(get_db)):
    return db.query(Experiment).all()

@router.get("/{experiment_id}", response_model=ExperimentResponse)
def get_experiment(experiment_id: int, db: Session = Depends(get_db)):
    experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not experiment:
        raise HTTPException(status_code=404, detail="Expérience introuvable")
    return experiment

@router.put("/{experiment_id}", response_model=ExperimentResponse)
def update_experiment(experiment_id: int, data: ExperimentUpdate, db: Session = Depends(get_db)):
    experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not experiment:
        raise HTTPException(status_code=404, detail="Expérience introuvable")
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(experiment, key, value)
    db.commit()
    db.refresh(experiment)
    return experiment

@router.delete("/{experiment_id}", status_code=204)
def delete_experiment(experiment_id: int, db: Session = Depends(get_db)):
    experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    if not experiment:
        raise HTTPException(status_code=404, detail="Expérience introuvable")
    db.delete(experiment)
    db.commit()