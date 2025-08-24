---

# 📧 Email Spam Classifier

A **Machine Learning powered Email/SMS Spam Classifier** built using **Python, Scikit-learn, and Streamlit**.
It helps to detect whether a given message/email is **Spam 🚨** or **Not Spam ✅** using **Multinomial Naive Bayes**.

---

## ✨ Features

* 📝 Text Preprocessing (tokenization, stopword removal, stemming)
* 🔢 TF-IDF Vectorization to convert text into numerical form
* 🤖 Machine Learning Model trained on a labeled spam dataset
* 🌐 Interactive Web App built with Streamlit
* 📊 Displays Accuracy & Precision of the model

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Scikit-learn** (for ML model)
* **NLTK** (for text preprocessing)
* **Streamlit** (for web interface)
* **Pickle** (for saving/loading model & vectorizer)

---

## 📂 Project Structure

email\_spam\_classifier/
│-- Spam\_Email\_app.py        # Streamlit application
│-- model.pkl                # Trained ML model
│-- vectorizer.pkl           # TF-IDF vectorizer
│-- requirements.txt         # Project dependencies
│-- README.md                # Project documentation
│-- spam\_classifier.ipynb    # Jupyter notebook (model training)

---

## ⚡ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/email_spam_classifier.git
cd email_spam_classifier
```

### 2️⃣ Create a Virtual Environment (Recommended)

```
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Mac/Linux
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App

```
streamlit run Spam_Email_app.py
```

---

## 🚀 Usage

1. Enter any **email or SMS message** in the text box.
2. Click **Predict**.

The app will display:

* ✅ **Not Spam** (Safe Message)
* 🚨 **Spam** (Suspicious/Promotional Message)

---

## 📊 Model Information

* **Algorithm Used:** Multinomial Naive Bayes
* **Accuracy:** \~97.8%
* **Precision:** \~98.3%
* **Dataset:** Publicly available `spam.csv` dataset

---

## 🔮 Future Improvements

* Add support for deep learning models (LSTM/Transformers)
* Enhance spam detection for harder cases (phishing, obfuscated text)
* Deploy as a live web service (Streamlit Cloud / HuggingFace / AWS)

---

## 🤝 Contributing

Pull requests are welcome! 🎉
For major changes, please open an issue first to discuss what you’d like to improve.

---

