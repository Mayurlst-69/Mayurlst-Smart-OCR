import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BACKEND_API_URL", "http://127.0.0.1:8000")

# Config front page (Tab)
st.set_page_config(page_title="Mayurlst OCR", page_icon="⚡", layout="wide")

# --- function for upload CSS ---
def local_css(file_name):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load style.css 
local_css("style.css")

st.markdown("<h1 class='hero-title'>Mayurlst OCR</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>Fastest Document Processing</p>", unsafe_allow_html=True)

# (Sidebar) user_maunal
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135692.png", width=100) # logo
    st.title("คำแนะนำการใช้งาน")
    st.info("""
    **ไฟล์ที่รองรับ:**
    - 📄 **PDF**: สำหรับ Resume
    - 🖼️ **JPG/PNG**: สำหรับไฟล์รูปภาพ
    """)
    st.warning("🔒 ข้อมูลที่อัปโหลดจะถูกประมวลผลและไม่ถูกบันทึกลง Server")

# Main
col1, col_center, col3 = st.columns([1.5, 3, 1.5])

with col_center:
    # เลือกฟังก์ชัน การทำงาน(Radio จะถูก CSS ปรับให้หน้าตาคล้าย Tabs แนวนอน)
    mode = st.radio(
        "โหมดการทำงาน",
        ("🔍 Smart OCR", "📄 PDF To Word", "📊 PDF To Excel", "🖼️ Picture To Word"),
        horizontal=True,
        label_visibility="collapsed" # ซ่อน Label เพื่อความคลีน
    )

# Files Validation
allowed_types = []
if "PDF" in mode or "OCR" in mode:
    allowed_types.extend(["pdf"])
if "Picture" in mode or "OCR" in mode:
    allowed_types.extend(["png", "jpg", "jpeg"])

uploaded_file = st.file_uploader(f"อัปโหลดเอกสารสำหรับโหมด '{mode}'", type=allowed_types)

if uploaded_file is not None:
        if st.button("✨ Start Processing", type="primary"):
            with st.spinner("Processing... please wait"):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                
                try:
                    # โหมด OCR
                    if "Smart OCR" in mode:
                        response = requests.post(f"{BASE_URL}/extract", files=files)
                        if response.status_code == 200:
                            st.success("✅ Extraction Complete!")
                            st.text_area("Text Output:", value=response.json()["extracted_text"], height=250)
                        else:
                            st.error(f"Error: {response.json().get('detail')}")
                            
                    # โหมด PDF to Word
                    elif "PDF To Word" in mode:
                        response = requests.post(f"{BASE_URL}/convert/pdf-to-word", files=files)
                        if response.status_code == 200:
                            st.success("✅ Conversion Complete!")
                            st.download_button("📥 Download Word File", data=response.content, file_name=uploaded_file.name.replace(".pdf", ".docx"))
                        else:
                            st.error(f"Error: {response.json().get('detail')}")
                            
                    # โหมด PDF to Excel
                    elif "PDF To Excel" in mode:
                        response = requests.post(f"{BASE_URL}/convert/pdf-to-excel", files=files)
                        if response.status_code == 200:
                            st.success("✅ Conversion Complete!")
                            st.download_button("📥 Download Excel File", data=response.content, file_name=uploaded_file.name.replace(".pdf", ".xlsx"))
                        else:
                            st.warning("No tables found in this PDF.")
                            
                    # โหมด Picture to Word
                    elif "Picture To Word" in mode:
                        response = requests.post(f"{BASE_URL}/convert/image-to-word", files=files)
                        if response.status_code == 200:
                            st.success("✅ Conversion Complete!")
                            st.download_button("📥 Download Word File", data=response.content, file_name=uploaded_file.name.split(".")[0] + ".docx")
                        else:
                            st.error(f"Error: {response.json().get('detail')}")

                except requests.exceptions.ConnectionError:
                    st.error("🚨 Cannot connect to Backend. Please ensure FastAPI is running.")

# Footer Section
st.markdown("<br><br><br><p style='text-align: center; color: gray; font-size: 0.9rem;'>The internal solution of choice for your departments</p>", unsafe_allow_html=True)
