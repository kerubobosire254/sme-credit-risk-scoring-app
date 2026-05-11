# 🧠 SME Credit Risk Scoring Platform

An AI-powered credit risk intelligence system that evaluates SMEs using financial data, predicts probability of default, 
and generates explainable credit reports with behavioural insights and industry benchmarking.


## 🚀 Project Overview

This system is designed to simulate a real-world credit underwriting engine used in fintech and lending institutions.

It enables users to:
- Upload SME financial data (CSV / Excel)
- Automatically engineer financial risk features
- Predict Probability of Default (PD)
- Generate an interpretable credit score
- Classify SMEs into behavioural risk personas
- Compare performance against industry benchmarks
- Download a structured credit risk report

## 🧠 Key Features

### 📊 1. Credit Risk Prediction
- Predicts Probability of Default using a trained ML model (XGBoost pipeline)
- Converts PD into an intuitive credit score (0–1000 scale)

### ⚙️ 2. Dynamic Feature Engineering
Automatically derives financial risk indicators from raw SME data:

- Debt-to-Income Ratio  
- Profit Margin  
- Cash Flow Variability  
- Revenue Growth Rate  
- Stress Index  
- Liquidity Risk  
- Payment Stress  

Handles missing or incomplete data using adaptive imputation strategies.

### 🧾 3. SME Behavioural Personas
Classifies businesses into interpretable risk segments:

- Stable SMEs  
- Growth SMEs  
- Seasonal SMEs  
- Distressed SMEs  

### 🏭 4. Industry Benchmarking
Compares SME performance against estimated industry averages for:

- Profitability  
- Leverage  
- Risk exposure  

### 📉 5. Risk Breakdown Explanation
Uses feature-level breakdowns to explain key drivers of credit risk:
- Debt pressure impact  
- Cashflow stress contribution  
- Payment history influence  

### 📄 6. Credit Report Generation
Automatically generates downloadable credit reports summarizing:
- Credit score  
- PD score  
- Risk category  
- Behavioural classification  
- Key risk drivers  

## 🏗️ System Architecture

```text
Raw SME Data
   ↓
Data Cleaning & Column Mapping
   ↓
Feature Engineering Layer
   ↓
Feature Alignment (Training Schema)
   ↓
ML Prediction (XGBoost Model)
   ↓
Explainability Layer (Risk Breakdown)
   ↓
Behavioural Clustering / Persona Tagging
   ↓
Report Generation (PDF/Text Output)

🧪 Tech Stack
Python 🐍
Streamlit (UI)
Pandas & NumPy (data processing)
Scikit-learn (ML pipeline)
XGBoost (risk model)
Plotly (visualizations)
Joblib (model persistence)

### Installation
git clone https://github.com/kerubobosire254/sme-credit-risk-platform.git
cd sme-credit-risk-platform

pip install -r requirements.txt

### Run the app
streamlit run app.py

###🧠Key Design Insight

This project bridges the gap between:

Raw SME financial data → Explainable credit intelligence system

It is designed with real-world constraints in mind:

Missing financial data
Non-standardized SME reporting
Need for interpretability in credit decisions

###📌 Future Improvements
SHAP-based explainability dashboard
Real-time SME risk scoring API
Industry-level dynamic benchmarking
Credit portfolio simulation engine
Database integration (PostgreSQL)
Cloud deployment (AWS / Azure)

⚠️ Disclaimer

This system is a prototype designed for educational and research purposes. It does not represent an official credit scoring system used by financial institutions.

💡 Author
Built by Kerubo Bosire
Actuarial Science | Risk Analytics | Machine Learning
