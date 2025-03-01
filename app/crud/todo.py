from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate

def get_todo(db: Session, todo_id: int) -> Optional[Todo]:
    return db.query(Todo).filter(Todo.id == todo_id).first()

def get_todos(db: Session, skip: int = 0, limit: int = 100) -> List[Todo]:
    return db.query(Todo).offset(skip).limit(limit).all()

def create_todo(db: Session, todo: TodoCreate) -> Todo:
    db_todo = Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: TodoUpdate) -> Optional[Todo]:
    db_todo = get_todo(db, todo_id)
    if db_todo:
        update_data = todo.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_todo, key, value)
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int) -> bool:
    db_todo = get_todo(db, todo_id)
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return True
    return False 