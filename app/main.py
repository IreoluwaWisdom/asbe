from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router

app = FastAPI()

app.include_router(router)

origins = [
    "http://localhost:8081",
    "https://attendance-system-rose.vercel.app",
    "http://192.168.43.182:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Face Recognition API with ONNX is running!"}