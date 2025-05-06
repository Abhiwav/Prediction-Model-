# Customer Churn Prediction Model

> **Not your usual Churn Model** 😎  
> **Includes a live Streamlit app you can try out!**

---

## Problem Statement / Main Aim of the Project

In banking, it can be difficult to predict whether a customer will repay a loan. This is where churn prediction becomes useful. This model helps predict the likelihood of a customer defaulting, aiding the bank in making informed decisions when approving or rejecting loan applications.

---

## Project Description

This project is designed as a learning setup for Git, GitHub, and machine learning model deployment.

It uses the **Lending Club dataset** from Kaggle to build a customer churn prediction model. The pipeline includes:

- `SimpleImputer` for handling missing numerical values  
- `TargetEncoder` for categorical features  
- `RandomForestClassifier` as the core model  

I used **pipelines** to automate preprocessing and model training.Additionally, I applied **GridSearchCV** to tune hyperparameters like `max_depth`, `n_estimators`, and others to achieve the best model performance.

The final model achieved an **accuracy of 82%**.

---

## Results

**Model Accuracy**: 82%  
**Validation Accuracy**: 0.8245  
**Validation AUC-ROC**: 0.7378  

**Classification Report**:

          precision    recall  f1-score   support

       0       0.83      0.98      0.90    167153
       1       0.67      0.20      0.31     40726

accuracy                           0.82    207879


---

## Streamlit App

I developed a **Streamlit app** that allows users to interact with the model in real time. Simply input the customer data, and the app will predict whether the customer is likely to churn.

Initially, the model was trained using the **top 20 features**. Later, I refined the model to use only the **top 10 features** to make it more user-friendly and reduce input fields. This made the app easier to use, though it led to a **2% drop in accuracy** — a trade-off for better usability.

> **Note**: The GitHub repository contains the version trained on 20 features. The 10-feature version of the code is not uploaded yet.

The Streamlit app is live and available 24/7. Feel free to test it anytime — just enter your data and get predictions instantly.

🔗 **Live App Link**: //mycustomerchurn99.streamlit.app/

---

## How to Use

1. Clone this repository  
2. Navigate to the project directory  
3. Install dependencies from `requirements.txt`  
4. Run `streamlit run app.py` to start the app locally  
5. Or, use the live app via the link above

---

## Author

**Abhinav Bora**

---


