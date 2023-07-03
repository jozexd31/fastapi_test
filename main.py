from typing import Union

import uvicorn
from fastapi import FastAPI
from logicaopenai.openai.testopenai import Document, inference

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/binary/{number}")
async def convert_to_binary(number: int):
    binary_number = bin(number)[2:]  # Convierte el número a binario
    return {"number": number, "binary": binary_number}




@app.post('/inference', status_code=200)
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    # Muestra la respuesta en la consola
    print("Respuesta del prompt:", response[0])
    return {
        'inference': response[0],
        'usage': response[1]
    }
if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=3200)
