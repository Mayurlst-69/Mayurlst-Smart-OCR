# 🚀 Smart OCR & Document Processing Studio

A modern, high-performance web application for extracting text from images and converting PDF documents into various formats (Word, Excel). Built with a premium "Glassmorphism" dark-mode UI.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit)
![EasyOCR](https://img.shields.io/badge/EasyOCR-AI_Powered-orange.svg)

## ✨ Features
- **🔍 Smart OCR:** Extract text from images (PNG, JPG) using AI (EasyOCR) with advanced pre-processing (CLAHE, Denoising).
- **📄 PDF to Word:** Seamlessly convert PDF documents into editable Word (`.docx`) files.
- **📊 PDF to Excel:** Automatically extract tabular data from PDFs into Excel (`.xlsx`) spreadsheets.
- **🖼️ Picture to Word:** Convert images with text directly into Word documents.
- **🎨 Premium UI:** Apple-inspired dark mode, animated mesh gradient background, and glassmorphism design.

## 🛠️ Architecture
This project is separated into two main microservices:
1. **Frontend:** Streamlit Community Cloud
2. **Backend (API):** FastAPI hosted on Render (Handles heavy AI and file processing)

## 💻 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/Smart-OCR-App.git](https://github.com/YOUR_GITHUB_USERNAME/Smart-OCR-App.git)
cd Smart-OCR-App