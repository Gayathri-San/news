import streamlit as st
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model("model.keras")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)


st.title(" Fake News Detection ")

user_input = st.text_area("Enter News Text")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter text")
    else:
        sequence = tokenizer.texts_to_sequences([user_input])

        padded = pad_sequences(sequence, maxlen=50)

        prediction = model.predict(padded)

        prob = prediction[0][0]

        if prob > 0.5:
            st.error(" FAKE NEWS ")
        else:
            st.success(" REAL NEWS ")