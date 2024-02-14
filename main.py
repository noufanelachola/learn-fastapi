from fastapi import FastAPI
from models import Todo

app = FastAPI()

todos = []

# Get all todos
@app.get("/todos/get")
async def getAllTodos():
    return{"todosList":todos}

# Create a todo
@app.post("/todo/create")
async def createTodo(todo:Todo):
    todos.append(todo)
    return{"message":"Todo has been successfully added"}

# 
@app.get("/todo/get/{todoId}")
async def getTodo(todoId:int):
    for todo in todos:
        if todo.id == todoId :
            return {"todo":todo}