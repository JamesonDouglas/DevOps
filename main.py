from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "bom dia"}

@app.get("/modificacao")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(a:0, b:1000)}
