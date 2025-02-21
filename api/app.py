from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

class InputPayload(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class OutputPayload(BaseModel):
    flower_type: str

loaded_model = pickle.load(open(model.pkl, 'rb'))


@app.post("/echo/")

def send_back_input(input: InputPayload):

    input_array = np.array([[input.sepal_length, input.sepal_width, input.petal_length, input.petal_width]])

    prediction = loaded_model.predict(input_array)

    return {"message": f"Input: {input.sepal_length} Sepal Length. {input.sepal_width} \
            Sepal Width. {input.petal_length} Petal Length. {input.petal_width} Pe