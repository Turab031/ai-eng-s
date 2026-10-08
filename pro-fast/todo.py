from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session

from database import SessionLocal, Base, engine
from models import TodoModel


# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


# -------------------------
# Pydantic Schemas
# -------------------------

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class TodoResponse(TodoBase):
    id: int

    class Config:
        orm_mode = True


# -------------------------
# Database Dependency
# -------------------------

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# -------------------------
# GET ALL TODOS
# -------------------------

@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos


# -------------------------
# GET TODO BY ID
# -------------------------

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):

    todo = db.query(TodoModel).filter(
        TodoModel.id == todo_id
    ).first()

    if todo:
        return todo

    return {"error": "todo id not found"}


# -------------------------
# CREATE TODO
# -------------------------

@app.post("/todos")
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db)
):

    new_todo = TodoModel(
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


# -------------------------
# DELETE TODO
# -------------------------

@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):

    todo = db.query(TodoModel).filter(
        TodoModel.id == todo_id
    ).first()

    if not todo:
        return {"error": "id not found"}

    db.delete(todo)
    db.commit()

    return {"message": "todo deleted successfully"}