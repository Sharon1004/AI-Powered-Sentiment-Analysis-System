import streamlit as st
import joblib
import os


# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="💬",
    layout="centered"
)


# Load trained model
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "models",
    "sentiment_pipeline.pkl"
)

model = joblib.load(MODEL_PATH)


# Title
st.title("💬 AI-Powered Sentiment Analysis")

st.write(
    "Enter a customer review and the machine learning model "
    "will classify its sentiment as Positive, Negative, or Neutral."
)


# User input
review = st.text_area(
    "Enter your review:",
    placeholder="Example: The product quality is excellent!",
    height=150
)


# Analyze button
if st.button("Analyze Sentiment"):

    if not review.strip():
        st.warning("Please enter a review.")

    else:
        prediction = model.predict([review])[0]

        # Get probability/confidence
        probabilities = model.predict_proba([review])[0]
        confidence = probabilities.max() * 100

        st.subheader("Prediction")

        if prediction == "Positive":
            st.success(f"😊 {prediction}")

        elif prediction == "Negative":
            st.error(f"😞 {prediction}")

        else:
            st.info(f"😐 {prediction}")

        st.write(
            f"**Confidence:** {confidence:.2f}%"
        )