from sqlalchemy import Column, String, Boolean, Text
from app.models.base import BaseModel

class Todo(BaseModel):
    __tablename__ = "todos"
    
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    is_completed = Column(Boolean, default=False) 