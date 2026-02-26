# 🚀 Smart OCR & Document Processing Studio

A modern, high-performance web application for extracting text from images and converting PDF documents into various formats (Word, Excel).

> 🌐 **Live Demo:** [Try Mayurlst OCR Here!](https://mayurlst-smart-ocr-mwibjbcv7uqfnbnztzbmmv.streamlit.app)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit)
![EasyOCR](https://img.shields.io/badge/EasyOCR-AI_Powered-orange.svg)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

## 💻 Tech Stack Overview

### 🎨 Frontend
- **Streamlit:** Fast and interactive web app framework.
- **Custom CSS:** Apple-inspired dark mode, animated mesh gradient background.

### ⚙️ Backend & API
- **FastAPI:** High-performance async API framework.
- **Uvicorn:** ASGI web server for Python.

### 🧠 AI & Computer Vision
- **EasyOCR (PyTorch):** Deep learning-based Optical Character Recognition for extracting text.
- **OpenCV (Headless):** Image pre-processing techniques (Grayscale, CLAHE, Denoising) to improve OCR accuracy.

### 📄 Document Processing
- **PyMuPDF & pdf2docx:** Fast PDF manipulation and conversion to editable Word documents.
- **pdfplumber & Pandas:** Extracting tables and structural data from PDFs into Excel (`.xlsx`) files.

### ☁️ Deployment & DevOps
- **Docker:** Containerization for a consistent production environment.
- **Hugging Face Spaces:** Hosting the heavy backend AI processes.
- **Streamlit Community Cloud:** Hosting the seamless frontend interface.

## ✨ Features
- **🔍 Smart OCR:** Extract text from images (PNG, JPG) with high precision.
- **📄 PDF to Word:** Seamlessly convert PDF documents into editable Word (`.docx`) files.
- **📊 PDF to Excel:** Automatically extract tabular data from PDFs into Excel spreadsheets.
- **🖼️ Picture to Word:** Convert images with text directly into Word documents.

## 🛠️ System Architecture
The application follows a decoupled **Microservices-inspired Architecture**:
1. **Frontend Client:** Hosted on Streamlit Cloud. It handles user inputs, file uploads, and renders the UI.
2. **REST API Server:** Hosted on Hugging Face Spaces. It receives files securely, processes them using AI models/libraries, and returns the converted files or extracted text back to the client.

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/Mayurlst/Mayurlst-Smart-OCR.git](https://github.com/Mayurlst/Mayurlst-Smart-OCR.git)
cd Mayurlst-Smart-OCR
```
### 2. Start the Backend (API)
```bash
cd backend
python -m venv venv_backend
source venv_backend/bin/activate  # On Windows: venv_backend\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
### 3. Start the Frontend (UI)
```bash
cd ../frontend
python -m venv venv_frontend
source venv_frontend/bin/activate  # On Windows: venv_frontend\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
---