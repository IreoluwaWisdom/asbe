from fastapi import FastAPI
from app.api import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Face Recognition API with ONNX is running!"}