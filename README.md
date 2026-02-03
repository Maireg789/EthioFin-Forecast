# 🇪🇹 EthioFin Forecast: Ethiopia Financial Inclusion Forecasting System

## Project Overview
Developed for **Selam Analytics**, this system tracks and forecasts Ethiopia's digital financial transformation. By bridging the gap between supply-side growth (Telebirr/M-Pesa) and demand-side reality (Global Findex), this tool provides actionable inclusion insights for the 2025–2027 period.

## ✅ Project Progress (Final Submission)
- [x] **Task 1: Data Exploration & Enrichment**
  - Enriched data with Telebirr (54M) and M-Pesa (10M) subscriber growth for 2022–2024.
- [x] **Task 2: Exploratory Data Analysis (EDA)**
  - Documented the "Usage Crossover" where P2P transfers surpassed ATM withdrawals.
- [x] **Task 3: Event Impact Modeling**
  - Developed a numeric **Association Matrix** linking policies (Digital ID) and launches to inclusion growth.
  - Visualized impacts via a Heatmap to identify key inclusion drivers.
- [x] **Task 4: 2025–2027 Forecasting**
  - Built an Event-Augmented model with three scenarios: **Optimistic (62%)**, **Base (53%)**, and **Pessimistic (50%)**.
- [x] **Task 5: Interactive Dashboard**
  - Deployed a **Streamlit App** with scenario selectors and interactive visualizations.

## 📂 Project Structure
- `dashboard/`: **app.py** - The interactive Streamlit dashboard.
- `data/`: Unified financial inclusion data and reference codes.
- `notebooks/`: 
  - `01_exploration_and_enrichment.ipynb`
  - `02_exploratory_data_analysis.ipynb`
  - `03_event_impact_modeling.ipynb`
  - `04_forecasting.ipynb`
- `reports/figures/`: Saved charts (Heatmaps, Forecasts, and Trajectories).
- `data_enrichment_log.md`: Provenance for external data sources.

## 📊 Strategic Insights
1. **The 60% Target:** Ethiopia can reach its national inclusion goal of 60% by 2027 only in the **Optimistic Scenario**, requiring full Fayda ID integration.
2. **Digital Dominance:** For the first time, digital P2P transfers have structurally overtaken cash-heavy ATM withdrawals.
3. **Slowdown Factors:** The 2021-2024 slowdown (+3pp) highlights that "Access" is limited by the lack of unique digital identities, not a lack of mobile money platforms.


The reason it looks like that is because you opened a code block with ```bash but never closed it with ```. This makes GitHub think the whole rest of the file is part of the code.
Copy and paste this exactly as it is below. I have fixed all the missing symbols and removed the "code Bash" text that was causing the error.

## 🚀 How to Run

### 1. Setup Environment
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate  
# Mac/Linux:
source .venv/bin/activate  

pip install -r requirements.txt
```  Launch Interactive Dashboard
```Bash
streamlit run dashboard/app.py
``` 
## 🛠️ Tech Stack
Analysis: Pandas, NumPy, SciPy
Visualization: Matplotlib, Seaborn, Plotly
Deployment: Streamlit
Version Control: Git/GitHub (Branch-based workflow)
