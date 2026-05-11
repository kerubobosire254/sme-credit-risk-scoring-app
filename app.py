# SME CREDIT RISK SCORING APP
# IMPORT LIBRARIES
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# PAGE CONFIGURATION
st.set_page_config(
    page_title="SME Credit Risk Platform",
    layout="wide"
)

# APP TITLE
st.title("SME Credit Risk Scoring Platform")

st.markdown("""
Upload SME financial data and get:

- Probability of Default
- Credit Score
- Risk Breakdown
- SME Behavioural Persona
- Industry Comparison
""")

# LOADING TRAINED MODEL
best_model = joblib.load('credit_risk_model.pkl')
kmeans_model = joblib.load('kmeans_model.pkl')
training_features = joblib.load("training_features.pkl")

# COLUMN STANDARDIZATION
COLUMN_MAPPING = {

    "monthly_revenue_avg": [
        "revenue",
        "sales",
        "turnover",
        "income"
    ],

    "monthly_expenses_avg": [
        "expenses",
        "costs",
        "monthly_expenses"
    ],

    "total_debt": [
        "debt",
        "liabilities",
        "loan_balance"
    ],

    "years_in_operation": [
        "business_age",
        "years_active"
    ],

    "num_transactions_per_month": [
        "transactions",
        "monthly_transactions"
    ],

    "avg_transaction_value": [
        "average_transaction"
    ],

    "late_payment_count": [
        "late_payments"
    ],

    "missed_payments": [
        "defaults",
        "missed_installments"
    ],

    "industry": [
        "sector"
    ],

    "location": [
        "business_location"
    ]
}

# STANDARDIZING COLUMNS FUNCTION
def standardize_columns(df):

    # Convert all columns to lowercase
    df.columns = df.columns.str.lower()

    # Remove spaces
    df.columns = df.columns.str.strip()

    # Dictionary for renaming
    rename_dict = {}

    # Looping through mappings
    for standard_name, variations in COLUMN_MAPPING.items():

        # Checking uploaded columns
        for col in df.columns:

            # If variation found
            if col in variations:

                # Rename column
                rename_dict[col] = standard_name

    # Rename dataframe columns
    df = df.rename(columns=rename_dict)

    return df

# FEATURE ENGINEERING FUNCTION

def engineer_features(df):

    # PROFIT MARGIN

    if (
        "monthly_revenue_avg" in df.columns
        and "monthly_expenses_avg" in df.columns
    ):

        df["profit_margin"] = (

            (
                df["monthly_revenue_avg"]
                - df["monthly_expenses_avg"]
            )

            /

            (df["monthly_revenue_avg"] + 1)

        )

    else:

        df["profit_margin"] = 0

    # DEBT TO INCOME RATIO

    if (
        "total_debt" in df.columns
        and "monthly_revenue_avg" in df.columns
    ):

        df["debt_to_income_ratio"] = (

            df["total_debt"]

            /

            (df["monthly_revenue_avg"] + 1)

        )

    else:

        df["debt_to_income_ratio"] = 0

    # CASH FLOW VARIABILITY

    df["cash_flow_variability"] = np.random.uniform(
        0.1,
        0.8,
        len(df)
    )

    # REVENUE GROWTH RATE

    df["revenue_growth_rate"] = np.random.uniform(
        -0.2,
        0.3,
        len(df)
    )

    # REPAYMENT HISTORY SCORE

    if "missed_payments" in df.columns:

        df["repayment_history_score"] = (

            100

            -

            (df["missed_payments"] * 10)

        )

    else:

        df["repayment_history_score"] = 80

    # REVENUE VOLATILITY

    df["revenue_volatility"] = (

        df["cash_flow_variability"]

        *

        df["monthly_revenue_avg"]

    )

    # EXPENSE SPIKES
    df["expense_spikes"] = np.random.randint(
        0,
        2,
        len(df)
    )

    # DECLINING REVENUE TREND

    df["declining_revenue_trend"] = np.where(

        df["revenue_growth_rate"] < 0,

        1,

        0
    )

    # CASH FLOW GAPS

    df["cash_flow_gaps"] = np.random.randint(
        0,
        5,
        len(df)
    )

    # STRESS INDEX

    df["stress_index"] = (

        df["debt_to_income_ratio"]

        +

        df["cash_flow_variability"]

        +

        df["missed_payments"]

    )

    # PAYMENT STRESS

    df["payment_stress"] = (

        df["late_payment_count"]

        +

        df["missed_payments"]

    )

    # LIQUIDITY RISK

    df["liquidity_risk"] = (

        df["cash_flow_variability"]

        *

        df["debt_to_income_ratio"]

    )

    # INDUSTRY RISK

    industry_risk_map = {

        "retail": 0.4,

        "services": 0.3,

        "manufacturing": 0.5,

        "agriculture": 0.45
    }

    # Convertin industries to lowercase
    df["industry"] = df["industry"].str.lower()

    # Mapping risk scores
    df["industry_risk"] = (

        df["industry"]

        .map(industry_risk_map)

        .fillna(0.35)
    )


    return df

# SME PERSONA

def assign_persona(df):

    personas = []

    # Looping through every SME
    for _, row in df.iterrows():

        # Stable businesses
        if (
            row["profit_margin"] > 0.25
            and row["debt_to_income_ratio"] < 0.5
        ):

            personas.append("stable")


        # Growth businesses
        elif (
            row["revenue_growth_rate"] > 0.15
        ):

            personas.append("growth")


        # Distressed businesses
        elif (
            row["stress_index"] > 2
        ):

            personas.append("distressed")


        # Seasonal businesses
        else:

            personas.append("seasonal")

    # Adding persona column
    df["business_persona"] = personas

    return df

# RISK LABEL FUNCTION

def get_risk_label(pd_probability):

    if pd_probability < 0.10:

        return "Low Risk"

    elif pd_probability < 0.30:

        return "Moderate Risk"

    else:

        return "High Risk"

# FILE UPLOADER

uploaded_file = st.file_uploader(

    "Upload SME Financial Data",

    type=["csv", "xlsx"]
)

if uploaded_file is not None:


    if uploaded_file.name.endswith(".csv"):

        df = pd.read_csv(uploaded_file)

    else:

        df = pd.read_excel(uploaded_file)

    st.subheader("Uploaded Data")

    st.dataframe(df.head())

    # STANDARDIZING COLUMNS

    df = standardize_columns(df)

    # FEATURE ENGINEERING

    df = engineer_features(df)

    # ASSIGN SME PERSONA

    df = assign_persona(df)

    # ALIGN FEATURES

    X = df.reindex(

        columns=training_features,

        fill_value=0
    )

    # MODEL PREDICTION

    pd_probability = (

        best_model.predict_proba(X)[0][1]

    )

    # CREDIT SCORE

    credit_score = int(

        (1 - pd_probability) * 1000

    )

    # RISK LABEL

    risk_label = get_risk_label(
        pd_probability
    )

    # DISPLAYING RESULTS

    st.subheader("Credit Risk Results")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Credit Score",
        credit_score
    )

    col2.metric(
        "Probability of Default",
        f"{pd_probability:.2%}"
    )

    col3.metric(
        "Risk Level",
        risk_label
    )

    # SME PERSONA

    st.subheader("SME Behavioural Persona")

    st.info(
        df["business_persona"].iloc[0]
    )

    # RISK BREAKDOWN

    st.subheader("Risk Breakdown")

    risk_data = pd.DataFrame({

        "Risk Factor": [

            "Debt To Income Ratio",

            "Stress Index",

            "Liquidity Risk",

            "Payment Stress"
        ],

        "Value": [

            df["debt_to_income_ratio"].iloc[0],

            df["stress_index"].iloc[0],

            df["liquidity_risk"].iloc[0],

            df["payment_stress"].iloc[0]
        ]
    })


    fig = px.bar(

        risk_data,

        x="Risk Factor",

        y="Value",

        title="Key Risk Drivers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # INDUSTRY BENCHMARK

    st.subheader("Industry Benchmark")

    benchmark = pd.DataFrame({

        "Metric": [

            "Profit Margin",

            "Debt To Income Ratio"
        ],

        "best_model": [

            df["profit_margin"].iloc[0],

            df["debt_to_income_ratio"].iloc[0]
        ],

        "Industry Average": [

            0.20,

            0.60
        ]
    })

    st.dataframe(benchmark)


else:

    st.info(
        "Please upload a CSV or Excel dataset."
    )