# MLHub - End-to-End MLOps Platform

MLHub is a centralized web platform designed to streamline, track, and deploy Machine Learning models from a single interface.

## Core Features

- Project Management: Organize datasets, experiments, and models into projects.
- Dataset Management: Upload CSV files, display data profiles and statistics, and manage versions.
- Experiment Tracking: Log hyperparameters, metrics (accuracy, F1-score, RMSE), duration, and dataset versions.
- Model Comparison: Compare models to select the best performer.
- Model Deployment: Serve selected models as REST APIs.
- Model Monitoring: Track requests, latency, errors, and data drift.

## Technology Stack

- Backend: FastAPI (Python 3.10+)
- Database: PostgreSQL
- Cache & Queue: Redis
- Testing: Pytest
- Containerization: Docker & Docker Compose

## Quick Start

### Prerequisites
- Python 3.10+
- Docker and Docker Compose (Optional)

### Run Locally

1. Clone the repository and navigate to the project directory.
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables in a `.env` file at the root:
   ```env
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/mlhub
   SECRET_KEY=mlhub-super-secret-key-change-this-in-production
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```
5. Run tests:
   ```bash
   python -m pytest
   ```
6. Start the API development server:
   ```bash
   uvicorn app.main:app --reload
   ```
   Interactive Swagger documentation will be available at: http://localhost:8000/docs

### Run with Docker

Build and run all services (API, DB, Redis) using Docker Compose:

```bash
docker-compose up -d --build
```

To stop all services:
```bash
docker-compose down
```

## Project Directory Structure

```text
mlhub/
├── app/
│   ├── api/routes/   # API route handlers (Auth, Datasets, Experiments)
│   ├── core/         # Settings, Database connections, Security logic
│   ├── models/       # SQLAlchemy database models
│   ├── schemas/      # Pydantic schemas for data validation
│   ├── services/     # Business logic
│   └── main.py       # FastAPI application entrypoint
├── tests/            # Test suite (Pytest)
├── Dockerfile        # Docker setup for API
├── docker-compose.yml# Docker Compose orchestration
└── requirements.txt  # Python package dependencies
```

## API Documentation

- POST /api/v1/auth/register - Register user
- POST /api/v1/auth/login - Login and retrieve JWT token
- POST /api/v1/datasets/ - Register dataset
- GET /api/v1/datasets/ - List datasets
- GET /api/v1/datasets/{id} - Get dataset details
- POST /api/v1/experiments/ - Log training experiment
- GET /api/v1/experiments/ - List all experiments
