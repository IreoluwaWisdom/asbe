from fastapi import APIRouter, File, UploadFile, Form, Request, Depends, BackgroundTasks
from services.email_service import send_email, EmailSchema
from services.face_recog import process_image
from sign_up import signUp
from sign_in import signIn
import shutil
import os
from services.db import connect_db, close_db

router = APIRouter()

def get_res():
    return {
        "status": False,
        "message": "We encountered an error processing your request.",
        "front_end_dev": "No action was carried out"
    }

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
async def test(res: dict = Depends(get_res)):
    conn = connect_db(res)
    close_db(conn)
    return {"filename": "Justatest.", "result": "Nothingtoseehere.", "res": res}

@router.post("/sign_in")
async def signInRouter(request: Request, res: dict = Depends(get_res)):
    post_data = await request.form()
    signIn(post_data, res)
    return res

@router.post("/send-email/")
async def send_email_endpoint(email: EmailSchema, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email)
    return {"message": f"Email to {email.email} is being sent!"}