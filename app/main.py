from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router
import os

print("MAIL_USERNAME:", os.getenv("AS_MAIL_USERNAME"))  # Should print a value
print("MAIL_PASSWORD:", os.getenv("AS_MAIL_PASSWORD"))  # Should be masked in logs


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