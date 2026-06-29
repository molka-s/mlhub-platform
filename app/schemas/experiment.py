from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class ExperimentCreate(BaseModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    dataset_id: int

class ExperimentUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    metrics: Optional[Dict[str, Any]] = None
    parameters: Optional[Dict[str, Any]] = None

class ExperimentResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    status: str
    metrics: Optional[Dict[str, Any]]
    parameters: Optional[Dict[str, Any]]
    dataset_id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True