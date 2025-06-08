import os
import streamlit as st
from PIL import Image
import cv2

st.title("👕 Virtual Try-On")

# Create 'static' directory if it doesn't exist
os.makedirs("static", exist_ok=True)

# File upload for person image
original_file = st.file_uploader("Upload Original Image (Person)", type=["jpg", "jpeg", "png"])
# File upload for clothing image
cloth_file = st.file_uploader("Upload Cloth Image", type=["jpg", "jpeg", "png"])

if original_file and cloth_file:
    # Save uploaded files
    original_path = os.path.join("static", "origin_web.jpg")
    cloth_path = os.path.join("static", "cloth_web.jpg")
    
    with open(original_path, "wb") as f:
        f.write(original_file.read())
    with open(cloth_path, "wb") as f:
        f.write(cloth_file.read())
    
    # Display uploaded images
    col1, col2 = st.columns(2)
    with col1:
        st.image(original_path, caption="Original Image", use_column_width=True)
    with col2:
        st.image(cloth_path, caption="Cloth Image", use_column_width=True)

    # Run the model
    with st.spinner("Processing... Please wait."):
        os.system("python main.py")

    # Display result
    result_path = "./static/finalimg.png"
    if os.path.exists(result_path):
        st.success("Try-on result generated successfully!")
        st.image(result_path, caption="Virtual Try-On Result", use_column_width=True)
    else:
        st.error("Failed to generate try-on result. Please check model setup.")
