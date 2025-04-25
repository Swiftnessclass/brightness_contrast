import streamlit as st
import cv2
import numpy as np


st.title("🎛️ Gamma Correction Tool")
st.write("Adjust the gamma to control image brightness using a power-law transformation.")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Gamma slider
gamma = st.slider("Gamma", min_value=0.1, max_value=3.0, value=1.0, step=0.1)

def gamma_correction(img, gamma_value):
    # Normalize image
    normalized = img / 255.0
    # Apply gamma correction
    corrected = np.power(normalized, gamma_value)
    # Scale back
    return np.uint8(corrected * 255)

if uploaded_file:
    # Read image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Apply gamma correction
    corrected_img = gamma_correction(image_rgb, gamma)

    # Show original and corrected
    st.subheader("Original Image")
    st.image(image_rgb, use_column_width=True)

    st.subheader(f"Gamma Corrected Image (Gamma = {gamma})")
    st.image(corrected_img, use_column_width=True)

