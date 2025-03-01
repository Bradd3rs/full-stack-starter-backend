from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base Todo schema with common attributes
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False

# Schema for creating a new Todo
class TodoCreate(TodoBase):
    pass

# Schema for updating an existing Todo
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

# Schema for returning a Todo from the API
class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 