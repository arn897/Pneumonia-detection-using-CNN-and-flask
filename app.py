# app.py
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ----------------------------
# Streamlit page configuration
st.set_page_config(
    page_title="Pneumonia Detection",
    page_icon="🫁",
    layout="centered"
)

st.title("🫁 Pneumonia Detection from Chest X-ray")
st.write(
    "Upload a chest X-ray image to predict whether it shows Pneumonia or is Normal. "
    "The model also shows prediction confidence and uncertainty warnings."
)

# ----------------------------
# Load model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(
        r"C:\Users\rarna\OneDrive\Desktop\project\project\models\pneumonia_model.h5"
    )
    # Build model once to avoid input errors
    dummy_input = np.zeros((1, 120, 120, 3), dtype=np.float32)
    model.predict(dummy_input)
    return model

model = load_model()

# ----------------------------
# Preprocess image
def preprocess_image(image):
    img = image.convert("RGB")
    img = img.resize((120, 120))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# ----------------------------
# Image uploader
uploaded_file = st.file_uploader(
    "Choose a chest X-ray image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=300)

    img_array = preprocess_image(image)

    # ----------------------------
    # Prediction
    pred_prob = model.predict(img_array)[0][0]

    # Dynamic threshold
    threshold = 0.7  # can tune between 0.6-0.8 to reduce false positives
    pred_class = "Pneumonia" if pred_prob >= threshold else "Normal"

    st.subheader(f"Prediction: {pred_class} ({pred_prob*100:.2f}% confidence)")

    # Warning for uncertainty
    lower_uncertain = 0.4
    upper_uncertain = 0.6
    if lower_uncertain < pred_prob < upper_uncertain:
        st.warning(
            "⚠️ Prediction is uncertain! The probability is close to 50%. "
            "Consider retesting or consulting a medical professional."
        )
