import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

# Page configuration
st.set_page_config(page_title="Gamma Correction Tool", page_icon="🎛️", layout="centered")

st.markdown("## 🎛️ Gamma Correction Tool")
st.markdown("Enhance your image brightness using a simple **power-law (gamma)** transformation! Adjust the slider and see the magic happen ✨")

st.markdown("---")

# Image uploader
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

# Gamma slider
gamma = st.slider("🔆 Adjust Gamma", min_value=0.1, max_value=3.0, value=1.5, step=0.1, help="Higher gamma brightens the image, lower gamma darkens it")

def gamma_correction(img, gamma_value):
    normalized = img / 255.0
    corrected = np.power(normalized, gamma_value)
    return np.uint8(corrected * 255)

if uploaded_file:
    # Read and decode the image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Apply gamma correction
    corrected_img = gamma_correction(image_rgb, gamma)

    # Display original and corrected side by side
    st.markdown("###  Image Preview")
    col1, col2 = st.columns(2)
    with col1:
        st.caption(" Original Image")
        st.image(image_rgb, use_column_width=True)
    with col2:
        st.caption(f" Gamma Corrected (γ = {gamma})")
        st.image(corrected_img, use_column_width=True)

    # Convert to PNG for download
    corrected_pil = Image.fromarray(corrected_img)
    buf = BytesIO()
    corrected_pil.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Download button
    st.markdown("### 📥 Download Your Result")
    st.download_button(
        label="Download Corrected Image",
        data=byte_im,
        file_name="gamma_corrected.png",
        mime="image/png",
        help="Click to download the adjusted image in PNG format"
    )

    st.success("✨ All done! Adjust the slider for a different effect.")
