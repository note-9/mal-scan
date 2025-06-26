from sqlmodel import SQLModel, Field
from typing import Optional
import datetime
from sqlalchemy import Column, JSON  # ✅ use Column directly

class File(SQLModel, table=True):
    id: str = Field(primary_key=True)
    filename: str
    status: str = "PROCESSING"
    report: Optional[dict] = Field(default=None, sa_column=Column(JSON))  # ✅ use Column(JSON)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
