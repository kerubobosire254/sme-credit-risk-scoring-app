# 🧠 SME Credit Risk Intelligence Platform

Small and Medium Enterprises (SMEs) are the backbone of emerging economies, driving employment, innovation, and economic growth. 
Yet despite their importance, access to affordable credit remains one of their biggest challenges.

Traditional lending systems were never built for modern SMEs.

Most financial institutions still rely heavily on:
- Collateral-based lending
- Manual underwriting
- Static financial ratios
- Incomplete financial statements

This creates a major visibility problem.

Lenders struggle to distinguish genuinely risky businesses from SMEs that simply lack formal or structured financial records. 
As a result:
- High-potential SMEs are denied financing
- Loan approvals become slow and inconsistent
- Risk pricing becomes inefficient
- Credit teams spend excessive time on manual analysis
- Informal businesses remain financially excluded

The challenge is not the absence of viable SMEs.  
The challenge is the absence of intelligent, explainable systems capable of understanding incomplete and non-traditional business data.

# 💡 Solution

The SME Credit Risk Intelligence Platform is an AI-driven underwriting and risk analytics system designed to transform raw SME financial data into actionable credit intelligence.

The platform combines:
- Machine Learning risk prediction
- Financial feature engineering
- Behavioural risk segmentation
- Explainable AI principles
- Industry-relative benchmarking

to generate transparent, data-driven lending insights.

Rather than replacing underwriters, the platform augments decision-making by providing:
- Probability of Default (PD) estimation
- Interpretable credit scoring
- Risk driver analysis
- SME behavioural profiling
- Automated credit assessment reports

Built specifically for real-world SME environments, the platform is designed to handle:
- Incomplete financial records
- Semi-structured business data
- Informal SME operational patterns
- Limited credit history environments

# 🚀 Project Overview

This platform simulates a real-world SME underwriting engine used in fintech and lending institutions.

Users can:
- Upload SME financial data (CSV / Excel)
- Automatically engineer financial risk features
- Predict Probability of Default (PD)
- Generate interpretable credit scores
- Classify SMEs into behavioural personas
- Compare SME performance against industry benchmarks
- Download structured credit risk reports

# 🧠 Key Capabilities

## 📊 AI-Powered Credit Risk Prediction
- Predicts Probability of Default (PD) using an XGBoost-based ML pipeline
- Converts model outputs into an interpretable credit score
- Categorizes SMEs into risk bands

## ⚙️ Intelligent Financial Feature Engineering

Automatically derives risk indicators from raw SME data, including:
- Debt-to-Income Ratio
- Profit Margin
- Revenue Growth
- Cash Flow Stability
- Liquidity Pressure
- Payment Stress
- Financial Stress Indicators

The platform also supports adaptive handling of missing or incomplete SME financial records.

## 🧠 Behavioural SME Segmentation

Classifies SMEs into behavioural risk personas such as:
- Stable SMEs
- Growth SMEs
- Seasonal SMEs
- Distressed SMEs

This enables lenders to move beyond static scoring toward behavioural risk understanding.

## 🏭 Industry Benchmarking

Compares SME performance against industry-level reference metrics for:
- Profitability
- Leverage
- Liquidity
- Risk exposure

This helps contextualize SME performance relative to peers.

## 🔍 Explainable Risk Intelligence

Provides transparent breakdowns of the major drivers influencing credit risk, including:
- Debt pressure
- Cash flow instability
- Repayment behaviour
- Revenue deterioration

Designed to support explainable and auditable lending decisions.

## 📄 Automated Credit Risk Reporting

Generates downloadable risk reports containing:
- Credit Score
- PD Score
- Risk Classification
- SME Persona
- Key Risk Drivers
- Financial Risk Summary

# 🏗️ System Architecture

```text
Raw SME Financial Data
        ↓
Data Cleaning & Standardization
        ↓
Dynamic Feature Engineering
        ↓
Feature Alignment Layer
        ↓
Machine Learning Risk Prediction
        ↓
Explainability & Risk Interpretation
        ↓
Behavioural Segmentation
        ↓
Industry Benchmarking
        ↓
Credit Risk Report Generation
```

# 🧪 Technology Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn, XGBoost |
| Visualization | Plotly |
| Model Persistence | Joblib |

# 🚀 Core Features

- CSV / Excel SME data upload
- Automated financial preprocessing
- Real-time risk scoring
- Explainable AI risk breakdowns
- Behavioural SME classification
- Industry benchmarking dashboard
- Scenario-based risk simulation
- Downloadable PDF risk reports

# 📌 Real-World Design Considerations

This system was built with practical SME lending constraints in mind:
- Missing financial records
- Informal business activity
- Non-standard reporting formats
- Need for underwriting transparency
- Explainability requirements in financial decision-making
  
# 🔮 Future Enhancements

- SHAP explainability dashboard
- Real-time risk scoring API
- Portfolio-level credit analytics
- Dynamic industry benchmarking
- PostgreSQL integration
- Cloud-native deployment (AWS / Azure)
- Alternative data integration (mobile money / transaction data)
- 
# 🚀 Live Demo
  Local URL: http://localhost:8502
  Network URL: http://192.168.1.184:8502
  
## Streamlit Cloud
https://sme-credit-risk-scoring-app-xadzpa4xvatoo2hk5zm5jj.streamlit.app/

# ⚙️ Installation

```bash
git clone https://github.com/kerubobosire254/sme-credit-risk-platform.git

cd sme-credit-risk-platform

pip install -r requirements.txt
```

# ▶️ Run the Application

```bash
streamlit run app.py
```

# ⚠️ Disclaimer

This project is a research and educational prototype designed to simulate SME credit underwriting workflows. It is not an official financial institution credit scoring system.

# 👩🏽‍💻 Author
**Kerubo Bosire**  
Actuarial Science | Risk Analytics | Machine Learning

