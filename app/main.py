from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes import auth, datasets, experiments, training
from app.models import user, dataset, experiment

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MLHub API",
    description="Plateforme MLOps — entraînement, suivi et déploiement de modèles",
    version="0.3.0"
)

app.include_router(auth.router, prefix="/api/v1")
app.include_router(datasets.router, prefix="/api/v1")
app.include_router(experiments.router, prefix="/api/v1")
app.include_router(training.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "MLHub API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}