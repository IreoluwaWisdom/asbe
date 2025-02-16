from fastapi import APIRouter, File, UploadFile, Form, Request
from app.face_recog import process_image
from app.sign_up import signUp
from app.sign_in import signIn
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

@router.get("/testav/")
async def test():
    return {"filename": "Justatest.", "result": "Nothingtoseehere."}

# Sample of all responses from the server
res = {
    "status": False,
    "message": "We encountered an error processing your request.",
    "front_end_dev": "No action was carried out" #For debugging purposes, probably should be removed later on.
}

@router.post("/signIn")
async def signInRouter(request: Request):
    global res
    post_data = await request.form()
    # res["message"] = "You have been signed in successfully."
    signIn(post_data, res)
    return res