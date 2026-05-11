# 🧠 SME Credit Risk Intelligence System

## 🚨 Problem Statement

Access to credit remains one of the biggest barriers to SME growth, especially in emerging markets.

Despite SMEs being the backbone of economic activity, most financial institutions struggle to accurately assess their creditworthiness due to:

- Incomplete or inconsistent financial records  
- Heavy reliance on collateral-based lending models  
- Lack of standardized financial reporting among SMEs  
- Limited visibility into cash flow behaviour and repayment patterns  
- High levels of informal or semi-formal financial activity  

As a result, many viable SMEs are incorrectly classified as high-risk, leading to:
- Credit under-approval  
- Over-reliance on manual underwriting  
- Slow loan processing cycles  
- Inefficient risk pricing  

## 💡 Solution

This project proposes an **AI-driven SME Credit Risk Intelligence Platform** that transforms raw SME financial data into:

- A probability of default (PD) score  
- An interpretable credit score  
- Behavioural risk segmentation  
- Industry-relative benchmarking  
- Explainable risk breakdowns  

The system is designed to replicate and enhance traditional credit underwriting by introducing:
- Data-driven feature engineering  
- Behavioural clustering of SMEs  
- Adaptive handling of incomplete financial data  
- Transparent, explainable risk outputs

# # 🧪 Tech Stack
- Python 🐍
- Streamlit (UI)
- Pandas & NumPy (data processing)
- Scikit-learn (ML pipeline)
- XGBoost (risk model)
- Plotly (visualizations)
- Joblib (model persistence)

# # 🚀 Live Demo
Local URL: http://localhost:8502
Network URL: http://192.168.1.184:8502

# # 🚀 Streamlit Cloud
https://sme-credit-risk-scoring-app-xadzpa4xvatoo2hk5zm5jj.streamlit.app/

## 🎯 Goal

To enable faster, fairer, and more accurate SME credit decisions by replacing rigid traditional scoring methods with a flexible, explainable machine learning-based risk engine.

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
