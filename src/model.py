# src/model.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Unified(BaseModel):
    uid: str
    source: str
    source_id: str
    title: Optional[str] = None
    body: Optional[str] = None
    completed: Optional[bool] = None
    author_id: Optional[str] = None
    fetched_at: datetime
