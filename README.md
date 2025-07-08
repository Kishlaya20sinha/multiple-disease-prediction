# 🏥 Multiple Disease Prediction System using Machine Learning

## 📌 Overview

This project is a **Streamlit-based web application** that predicts the likelihood of three diseases using trained Machine Learning models:

- 🩺 **Diabetes**
- ❤️ **Heart Disease**
- 🧠 **Parkinson's Disease**

The app allows users to input relevant medical information and receive instant predictions, making it a simple health assistant tool for awareness and early indication.

---

## 🚀 Features

- 🔍 User-friendly interface using Streamlit  
- 📊 Predicts 3 major diseases with different ML models  
- ✅ Input validation and error handling  
- 💾 Models loaded via `pickle` for fast inference  
- 🧮 Built-in ML logic without exposing model code in UI  

---

## 🧠 ML Models Used

| Disease         | Model Used                     | Dataset Source                   |
|----------------|----------------------------------|----------------------------------|
| Diabetes        | Logistic Regression / Random Forest | PIMA Indian Diabetes Dataset     |
| Heart Disease   | Random Forest / Logistic Regression | UCI Heart Disease Dataset        |
| Parkinson's     | SVM / Random Forest             | UCI Parkinson’s Disease Dataset  |

*You can modify the table based on the models you used.*

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Scikit-learn  
- Pickle  
- HTML/CSS (via Streamlit widgets)  

---

## 📁 Project Structure

📦 multiple-disease-prediction-streamlit-app
├── app.py
├── saved_models/
│ ├── diabetes_model.sav
│ ├── heart_disease_model.sav
│ └── parkinsons_model.sav
├── requirements.txt
└── README.md

---

## ▶️ Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/multiple-disease-prediction-streamlit-app.git
cd multiple-disease-prediction-streamlit-app
```

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv .venv
# Activate it:
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the App

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

[Live Demo](https://multiple-disease-prediction-2k5xyqhqhchfsuxsgonzii.streamlit.app/)

---

## ✨ Features

- Predicts multiple diseases including Diabetes, Heart Disease, and Parkinson’s.
- Simple and interactive UI built with Streamlit.
- Uses Scikit-learn models trained on public datasets.
- Instant prediction results after inputting user data.

---

## 📂 Dataset Info

- UCI ML Repository datasets
- Preprocessed CSV files used for training and testing.
- Feature engineering applied for model optimization.

---

## 👨‍💻 Author

**Kishlaya Sinha**  
📧 kishlaya20sinha@gmail.com  
🔗 | [GitHub](https://github.com/Kishlaya20sinha) | [LinkedIn](https://www.linkedin.com/in/kishlaya-sinha-9134a0211/)

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

- Scikit-learn  
- Streamlit  
- UCI ML Repository