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

# Get a todo
@app.get("/todo/get/{todoId}")
async def getTodo(todoId:int):
    for todo in todos:
        if todo.id == todoId :
            return {"todo":todo}
    return {"message":"No todos found"}

# Delete a todo
@app.delete("/todo/delete/{todoId}")
async def deleteTodo(todoId:int):
    for todo in todos:
        if todo.id == todoId :
            todos.remove(todo)
            return {"todo":todo}        
    return {"message":"No todos found"}

# Update a todo
@app.put("/todo/update/{todoId}")
async def updateTodo(todoId:int,todo_Obj:Todo):
    for todo in todos:
        if todo.id == todoId:
            todo.id = todoId
            todo.item = todo_Obj.item
            return {"todo":todo}
    return {"message":"Couldnt update todo"}