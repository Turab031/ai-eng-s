from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv

app = FastAPI()
todos=[]


class Todo(BaseModel):
    id:int
    title:str
    description:Optional[str]=None
    completed:bool=False

@app.get("/todos")
def get_todos():
    return todos



@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo['id']==todo_id:
            return todo
    return {"error":"todo id not found"}



@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo.dict())
    # return the last todo
    return todos[-1]


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for todo in todos:
        if todo['id']==todo_id:
            todos.remove(todo)
            return {"message":"todo deleted successfully"}
    return {"error":"id not found"}