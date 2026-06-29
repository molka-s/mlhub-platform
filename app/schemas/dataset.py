from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DatasetCreate(BaseModel):
    name: str
    description: Optional[str] = None
    size_mb: Optional[float] = None

class DatasetUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class DatasetResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    file_path: Optional[str]
    size_mb: Optional[float]
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True