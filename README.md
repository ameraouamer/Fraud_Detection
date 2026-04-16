#  Fraud Detection System using Machine Learning

An end-to-end machine learning project for detecting fraudulent transactions, covering data preprocessing, model training, evaluation, and deployment with an interactive web app.

---

## 📌 Overview

This project builds a classification model to identify fraudulent transactions with a strong focus on **recall**, ensuring most fraud cases are detected.

Key challenges handled:
- Imbalanced dataset  
- Mixed feature types (numerical & categorical)  
- Proper preprocessing and evaluation  

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- **Streamlit (deployment & UI)**  

---

## 📂 Structure

```
Fraud_Detection/
├── data/
├── notebooks/
├── src/
├── app/              # Streamlit app
├── models/
├── requirements.txt
└── README.md
```

---

## 🔍 Pipeline

1. Data cleaning & preprocessing  
2. EDA (visualization & insights)  
3. Feature engineering (scaling + encoding)  
4. Model training (Logistic Regression)  
5. Evaluation (confusion matrix, classification report)  
6. Deployment with Streamlit  

---

##  Results

- High recall → detects most fraud cases  
- Balanced precision → limits false positives  

> Missing fraud is more costly than false alarms.

---

## 🚀 Run Locally

```bash
git clone https://github.com/your-username/Fraud_Detection.git
cd Fraud_Detection

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

---

##  Next Steps for now 

- Try advanced models (XGBoost, Random Forest)  
- Handle imbalance with SMOTE  
- Hyperparameter tuning  
- Deploy online (Streamlit Cloud / Docker)  