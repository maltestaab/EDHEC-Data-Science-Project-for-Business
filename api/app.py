from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputPayload(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/echo/")

def send_back_input(input: InputPayload):
    return {"message": f"Input: {input.sepal_length} Sepal Length. {input.sepal_width} \
            Sepal Width. {input.petal_length} Petal Length. {input.petal_width} Petal Width."}