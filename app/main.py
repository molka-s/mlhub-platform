from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes import auth

# Créer les tables automatiquement
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MLHub API",
    description="Plateforme MLOps — entraînement, suivi et déploiement de modèles",
    version="0.1.0"
)

# Inclure les routes
app.include_router(auth.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "MLHub API is running 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}