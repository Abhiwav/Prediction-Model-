import streamlit as st
import numpy as np
import pandas as pd  # Import pandas
import joblib

# Function to load the trained model
def load_model():
    return joblib.load("C:/Users/abhin/Desktop/loan_prediction_api/model/loan_model.pkl")  # Ensure this path is correct

def main():
    st.title("Customer Churn Prediction")
    st.write("Enter customer details to predict churn.")
    
    # Input Fields
    emp_title = st.text_input("Employment Title")
    debt_settlement_flag = st.radio("Debt Settlement Flag", ["Yes", "No"])  # Convert to binary
    sub_grade = st.selectbox("Sub Grade", ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5"])
    int_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=50.0, value=10.0)
    grade = st.selectbox("Grade", ["A", "B", "C", "D", "E", "F", "G"])
    term = st.selectbox("Term", ["36 months", "60 months"])
    issue_d = st.date_input("Issue Date")
    dti = st.number_input("Debt-to-Income Ratio", min_value=0.0, max_value=100.0, value=20.0)
    fico_range_low = st.number_input("FICO Range Low", min_value=300, max_value=850, value=650)
    fico_range_high = st.number_input("FICO Range High", min_value=300, max_value=900, value=700)
    
    # Convert Inputs to Model Format
    debt_settlement_flag = 1 if debt_settlement_flag == "Yes" else 0

    # Define column names exactly as used during training
    column_names = [
        "emp_title", "debt_settlement_flag", "sub_grade", "int_rate", "grade", 
        "term", "issue_d", "dti", "fico_range_low", "fico_range_high"
    ]

    # Convert input_data into a DataFrame
    input_data = pd.DataFrame([[
        emp_title, debt_settlement_flag, sub_grade, int_rate, grade, 
        term, issue_d, dti, fico_range_low, fico_range_high
    ]], columns=column_names)

    # Load model
    model = load_model()
    
    if st.button("Predict Churn"):
        try:
            prediction = model.predict(input_data)[0]
            result = "Churn" if prediction == 1 else "No Churn"
            st.write(f"### Prediction: {result}")
        except Exception as e:
            st.error(f"Error making prediction: {e}")

if __name__ == "__main__":
    main()
