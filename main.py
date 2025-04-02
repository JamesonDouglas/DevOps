from fastapi import FastAPI # type: ignore
import random

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "bom dia"}

@app.get("/teste")
async def teste():
    return {"teste": True, "num_aleatorio": random.randint(1, 100)}