from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/greet/")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

# Define a model for request body validation
class User(BaseModel):
    name: str
    age: int

@app.post("/users/")

def create_user(user: User):
    return {"message": f"User {user.name} of age {user.age} created!"}