import streamlit as st
from prediction_helper import predict

st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="🏥",
    layout="wide"
)

# --- Styling ---
st.markdown("""
<style>
    .main { padding-top: 20px; }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border: none;
        padding: 10px 32px;
        font-size: 15px;
        border-radius: 6px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    .result-box {
        background: #f0fdf4;
        border: 1px solid #86efac;
        border-radius: 8px;
        padding: 24px;
        text-align: center;
        margin-top: 16px;
    }
    .result-box h2 {
        color: #166534;
        font-size: 36px;
        margin: 0;
    }
    .result-box p {
        color: #4b5563;
        margin: 6px 0 0;
        font-size: 14px;
    }
    h3 {
        font-size: 16px;
        font-weight: 600;
        color: #111827;
        margin-bottom: 4px;
        border-bottom: 2px solid #e5e7eb;
        padding-bottom: 6px;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("🏥 Health Insurance Cost Predictor")
st.caption("Estimate your annual health insurance premium using Machine Learning.")
st.divider()

# --- Options ---
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['Non-Smoker', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Medical History', 'Diabetes', 'High blood pressure',
        'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
        'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# --- Personal Details ---
st.markdown("### Personal Details")
col1, col2, col3, col4 = st.columns(4)
with col1:
    age = st.number_input('Age', min_value=18, max_value=100, value=30, step=1)
with col2:
    gender = st.selectbox('Gender', categorical_options['Gender'])
with col3:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
with col4:
    number_of_dependents = st.number_input('Number of Dependents', min_value=0, max_value=20, step=1)

st.markdown("<br>", unsafe_allow_html=True)

# --- Employment & Finance ---
st.markdown("### Employment & Finance")
col1, col2, col3 = st.columns(3)
with col1:
    income_lakhs = st.number_input('Annual Income (₹ Lakhs)', min_value=0, max_value=200, step=1)
with col2:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])
with col3:
    region = st.selectbox('Region', categorical_options['Region'])

st.markdown("<br>", unsafe_allow_html=True)

# --- Health Information ---
st.markdown("### Health Information")
col1, col2, col3, col4 = st.columns(4)
with col1:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
with col2:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with col3:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])
with col4:
    genetical_risk = st.number_input('Genetical Risk (0–5)', min_value=0, max_value=5, step=1)

st.markdown("<br>", unsafe_allow_html=True)

# --- Insurance Plan ---
st.markdown("### Insurance Plan")
col1, col2 = st.columns([1, 3])
with col1:
    insurance_plan = st.selectbox('Plan Type', categorical_options['Insurance Plan'])

st.divider()

# --- Predict Button ---
col_a, col_b, col_c = st.columns([2, 1, 2])
with col_b:
    predict_btn = st.button('Predict Premium')

# --- Prediction Logic ---
if predict_btn:
    input_dict = {
        'Age': age,
        'Number of Dependents': number_of_dependents,
        'Income in Lakhs': income_lakhs,
        'Genetical Risk': genetical_risk,
        'Insurance Plan': insurance_plan,
        'Employment Status': employment_status,
        'Gender': gender,
        'Marital Status': marital_status,
        'BMI Category': bmi_category,
        'Smoking Status': smoking_status,
        'Region': region,
        'Medical History': medical_history
    }

    with st.spinner('Running prediction...'):
        prediction = predict(input_dict)

    st.success("Prediction generated successfully!")

    col_l, col_m, col_r = st.columns([1, 2, 1])
    with col_m:
        st.markdown(f"""
        <div class="result-box">
            <p>💰 Estimated Annual Premium</p>
            <h2>₹ {prediction} / year</h2>
            <p>Plan: <strong>{insurance_plan}</strong> &nbsp;|&nbsp; This is an estimate only.</p>
        </div>
        """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("⚠️ This tool provides estimates only and should not be treated as financial advice.")