from importlib import import_module


FastAPI = import_module("fastapi").FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
