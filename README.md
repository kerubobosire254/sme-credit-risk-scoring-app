# SME Credit Risk Intelligence Platform

> XGBoost-powered probability of default estimation, behavioural SME profiling, and explainable credit scoring — built for East African fintech and lending environments.

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-ML_Engine-0066CC?style=flat)](https://xgboost.readthedocs.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)

**Live Demo →** https://sme-credit-risk-scoring-app-xadzpa4xvatoo2hk5zm5jj.streamlit.app/

### SNIPPET OF THE APP

<img width="1260" height="564" alt="image" src="https://github.com/user-attachments/assets/7e34c81e-5eac-4fa7-8172-40141c27ee2c" />

## The Problem

Traditional credit systems were not built for SMEs.

Most lenders still rely on collateral, manual underwriting, and static financial ratios — tools designed for large corporates with audited books and credit histories. For the 50 million+ SMEs across Sub-Saharan Africa, this creates a systemic exclusion problem:

- High-potential businesses are denied financing due to informal records
- Loan approvals are slow, inconsistent, and difficult to audit
- Risk teams spend excessive time on manual analysis with no standardised framework
- Lenders cannot distinguish genuinely risky SMEs from those that simply lack structured documentation

**The gap is not the absence of viable SMEs. It is the absence of intelligent systems capable of interpreting non-traditional business data.**

## Solution

The SME Credit Risk Intelligence Platform is an AI-driven underwriting engine that transforms raw SME financial inputs into structured, explainable credit intelligence.

It combines machine learning risk prediction, dynamic feature engineering, behavioural segmentation, and industry benchmarking to generate lending decisions that are fast, transparent, and auditable — without replacing the underwriter.

## Key Features

### AI-Powered Credit Scoring
- XGBoost classifier outputs a calibrated **Probability of Default (PD)** between 0 and 1
- PD converts to an interpretable **credit score** on a 100–1000 scale
- Automatic classification into **Low / Moderate / High** risk bands

### Intelligent Feature Engineering
Derives 15+ risk indicators from raw SME inputs, including:

| Feature | Description |
|---|---|
| `debt_to_income_ratio` | Total debt relative to monthly revenue |
| `profit_margin` | Net margin after expenses |
| `stress_index` | Composite financial pressure score |
| `liquidity_risk` | Cash flow exposure to debt obligations |
| `payment_stress` | Late + missed payment combined signal |
| `cash_flow_variability` | Expense stability relative to revenue |
| `repayment_history_score` | Normalised payment track record |

### Behavioural SME Segmentation
SMEs are classified into four behavioural personas based on financial patterns:

| Persona | Signal |
|---|---|
| 🏛️ **Stable SME** | Consistent margins, low leverage, strong repayment |
| 🚀 **Growth SME** | Expanding revenue, elevated DTI acceptable at stage |
| 🔄 **Seasonal SME** | Cyclical revenue — repayment timing matters |
| ⚠️ **Distressed SME** | High stress index, payment irregularities, compressed margins |

### Industry Benchmarking
Radar chart comparison of SME performance against industry-level reference metrics across profitability, leverage, repayment score, and liquidity — contextualising risk relative to peers.

### Batch Portfolio Mode
Upload a CSV or Excel file of multiple SMEs and get:
- Portfolio-wide risk distribution and score histogram
- Credit Score vs PD scatter plot by risk band
- Full drill-down into any individual SME from the batch

### Automated Underwriter Summary
Natural-language credit memo generated per SME — including margin analysis, DTI assessment, payment behaviour flags, and a structured lending recommendation.

## System Architecture

```
Raw SME Financial Data (CSV / Excel / Form Input)
        ↓
Column Standardisation Layer
        ↓
Dynamic Feature Engineering (15+ derived features)
        ↓
Feature Alignment (training schema enforcement)
        ↓
XGBoost Risk Prediction  →  Probability of Default
        ↓
Credit Score Derivation  +  Risk Band Classification
        ↓
Behavioural Segmentation  +  Industry Benchmarking
        ↓
Underwriter Summary  +  Drill-Down Report
```

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Language | Python 3.11 |
| ML Model | XGBoost + Scikit-learn |
| Feature Engineering | Pandas, NumPy |
| Visualisation | Plotly |
| Model Persistence | Joblib |

## Getting Started

```bash
git clone https://github.com/kerubobosire254/sme-credit-risk-scoring-app.git
cd sme-credit-risk-scoring-app
pip install -r requirements.txt
streamlit run app.py
```

**Required model files** :
```
credit_risk_model.pkl
kmeans_model.pkl
training_features.pkl
```

### Input Schema

Your CSV/Excel file should include these columns (flexible naming supported):

```
sme_name, monthly_revenue_avg, monthly_expenses_avg, total_debt,
years_in_operation, num_transactions_per_month, avg_transaction_value,
late_payment_count, missed_payments, industry, location
```

The platform handles non-standard column names via an automatic mapping layer.

---

## Design Considerations

This system was built with real SME lending constraints in mind:

- **Incomplete records** — feature engineering degrades gracefully with missing inputs
- **Informal activity** — derived features proxy cash flow behaviour without requiring full accounts
- **Explainability** — every score has a visible risk driver breakdown; no black-box outputs
- **Auditability** — underwriter summaries are reproducible and data-grounded

## Roadmap

- [ ] SHAP explainability dashboard
- [ ] Real-time scoring API (FastAPI)
- [ ] PDF credit report export
- [ ] Alternative data integration (M-Pesa / mobile money transaction feeds)
- [ ] PostgreSQL portfolio persistence
- [ ] Cloud deployment (AWS / Azure)
- [ ] Dynamic industry benchmark calibration

## Disclaimer

This is a research and educational prototype simulating SME credit underwriting workflows. It is not an official financial institution credit scoring system and should not be used as the sole basis for lending decisions.


## Author

**Kerubo Bosire**  
Actuarial Science · Risk Analytics · Machine Learning  
[GitHub](https://github.com/kerubobosire254) · [LinkedIn](https://linkedin.com/in/kerubo-bosire-364523283)

