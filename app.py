import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch
#from pyngrok import ngrok

# Load the model and tokenizer
model = BertForSequenceClassification.from_pretrained("saved_model")
tokenizer = BertTokenizer.from_pretrained("saved_model")

# Streamlit UI
st.title("Spam Detection AI")
user_input = st.text_input("Enter your text:")

if st.button("Check"):
    if user_input.strip() == "":
        st.write("Please enter some text.")
    else:
        # Tokenize the input text
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True, max_length=512)

        # Perform prediction
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()

        # Map the predicted class to spam or not spam
        result = "Spam" if predicted_class == 1 else "Not Spam"
        st.write(f"Result: {result}")

# Set up ngrok to tunnel the local Streamlit server
#public_url = ngrok.connect(addr=8501, proto="http")  # Specify `addr` and protocol
#print(f"Public URL: {public_url}")
