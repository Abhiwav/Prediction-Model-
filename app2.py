import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Set background and element styles
def add_styles():
    st.markdown("""
        <style>
        /* Page background */
        .stApp {
            background-color: #f8f8f2;
        }

        /* Title styling */
        h1 {
            color: #333333;
            font-weight: bold;
        }

        /* Widget label styling */
        label, .stRadio > label, .stSelectbox > label, .stDateInput > label {
            font-weight: bold !important;
            color: #222 !important;
        }

        /* Input and dropdown text visibility */
        .stSelectbox div, .stTextInput input, .stNumberInput input, .stDateInput input {
            color: black !important;
        }

        /* Cover image spacing */
        .cover-image {
            margin-bottom: 20px;
            border-radius: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

# Load the trained model
def load_model():
    return joblib.load("C:/Users/abhin/Desktop/loan_prediction_api/model/loan_model.pkl")

def main():
    # Apply styles first
    add_styles()

    # Show cover image like a LinkedIn banner
    st.image("BACKPIC.jpg", use_container_width=True)

    st.title("📉 Customer Churn Prediction")
    st.markdown("#### 🧾 Enter customer details to predict churn")


    # Input layout
    col1, col2 = st.columns(2)

    with col1:
        emp_title = st.text_input("Employment Title")
        sub_grade = st.selectbox("Sub Grade", 
            ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5"])
        int_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=50.0, value=10.0)
        fico_range_low = st.number_input("FICO Range Low", min_value=300, max_value=850, value=650)

    with col2:
        debt_settlement_flag = st.radio("Debt Settlement Flag", ["Yes", "No"])
        grade = st.selectbox("Grade", ["A", "B", "C", "D", "E", "F", "G"])
        term = st.selectbox("Term", ["36 months", "60 months"])
        issue_d = st.date_input("Issue Date")
        dti = st.number_input("Debt-to-Income Ratio", min_value=0.0, max_value=100.0, value=20.0)
        fico_range_high = st.number_input("FICO Range High", min_value=300, max_value=900, value=700)

    # Convert categorical
    debt_settlement_flag_bin = 1 if debt_settlement_flag == "Yes" else 0

    column_names = [
        "emp_title", "debt_settlement_flag", "sub_grade", "int_rate", "grade", 
        "term", "issue_d", "dti", "fico_range_low", "fico_range_high"
    ]

    input_data = pd.DataFrame([[ 
        emp_title, debt_settlement_flag_bin, sub_grade, int_rate, grade, 
        term, issue_d, dti, fico_range_low, fico_range_high
    ]], columns=column_names)

    model = load_model()

    if st.button("🔍 Predict Churn"):
        try:
            prediction = model.predict(input_data)[0]
            result = "🚨 Churn" if prediction == 1 else "✅ No Churn"
            st.success(f"### Prediction Result: {result}")
            st.balloons()
        except Exception as e:
            st.error(f"Prediction failed: {e}")

if __name__ == "__main__":
    main()
