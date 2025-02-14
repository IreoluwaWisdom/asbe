from fastapi import APIRouter, File, UploadFile
from app.face_recog import process_image
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/recognize/")
async def recognize_face(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_image(file_path)

    return {"filename": file.filename, "result": result}

@router.post("/testav/")
async def test():
    return {"filename": "Justatest.", "result": "Nothingtoseehere."}