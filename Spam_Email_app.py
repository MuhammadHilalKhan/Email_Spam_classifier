import streamlit as st
import pickle
import string
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk

# Initialize stemmer
ps = PorterStemmer()

# Preprocessing function
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(ps.stem(i))
    return " ".join(y)

# Load vectorizer & model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Spam Classifier", page_icon="📧", layout="centered")

# Custom CSS for better interface
st.markdown("""
    <style>
    body {
        background-color: #f4f7f9;
    }
    .main-title {
        text-align: center;
        color: #2c3e50;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .stTextArea textarea {
        background-color: #ffffff;
        border: 2px solid #2980b9;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    .prediction-box {
        background-color: #ecf0f1;
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
        border: 2px solid #2980b9;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
    }
    .info-box {
        background-color: #ffffff;
        border: 2px solid #27ae60;
        border-radius: 12px;
        padding: 15px;
        margin-top: 25px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .info-title {
        font-size: 20px;
        font-weight: bold;
        color: #27ae60;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h1 class='main-title'>📧 Email/SMS Spam Classifier</h1>", unsafe_allow_html=True)

# Input box
input_sms = st.text_area("✉️ Enter the Message:")

if st.button('🔍 Predict'):
    # 1. Preprocess
    transformed_sms = transform_text(input_sms)
    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. Predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.markdown("<div class='prediction-box' style='color: red;'>🚨 Spam</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='prediction-box' style='color: green;'>✅ Not Spam</div>", unsafe_allow_html=True)

# Info box about model
st.markdown("""
<div class="info-box">
    <div class="info-title">📊 Model Information</div>
    <p><b>Algorithm Used:</b> Multinomial Naive Bayes</p>
    <p><b>Accuracy:</b> 97.8%</p>
    <p><b>Precision:</b> 98.3%</p>
</div>
""", unsafe_allow_html=True)

