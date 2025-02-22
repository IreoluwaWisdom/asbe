# Face Recognition Backend (FastAPI)

This is a FastAPI backend for handling face recognition using ONNX models.

## 🚀 Installation & Setup

1. **Clone the Repository**
   ```sh
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```
2. **Create and Activate a Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```sh
   # First copy .example.env to .env
   copy .example.env .env
   # Next update the .env file with the required missing fields, and you are done.
   ```

5. **Run the FastAPI Server**
   ```sh
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```


## **📌 API Endpoints**

- POST `/recognize` → Upload an image for face recognition.
- POST `/signUp` -> signUp user.
- POST `/signIn` -> signIn user.


## **🛠 Tech Stack**

- FastAPI for the API

- ONNX Runtime for face recognition

- NumPy & Pillow for image processing
