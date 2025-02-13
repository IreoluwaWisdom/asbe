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

4. **Run the FastAPI Server**
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```


## **📌 API Endpoints**

- POST `/recognize` → Upload an image for face recognition.


## **🛠 Tech Stack**

- FastAPI for the API

- ONNX Runtime for face recognition

- NumPy & Pillow for image processing
