# Ethiopia Financial Inclusion Forecasting System

## Project Overview
This project, developed for Selam Analytics, tracks and forecasts Ethiopia's digital financial transformation. It analyzes the gap between supply-side growth (mobile money) and demand-side reality (Global Findex account ownership) to provide stakeholders with actionable insights for 2025–2027.

## Current Progress (Interim Submission)
- [x] **Task 1: Data Exploration & Enrichment**
  - Analyzed the Unified Schema and identified temporal gaps.
  - Enriched data with Telebirr and M-Pesa subscriber growth (2022–2024).
- [x] **Task 2: Exploratory Data Analysis (EDA)**
  - Identified the +3pp growth slowdown (2021–2024).
  - Visualized the impact of major product launches (Telebirr, M-Pesa) vs. inclusion rates.
  - Documented the "Usage Crossover" where P2P transfers surpassed ATM withdrawals.

## Project Structure
- `.github/workflows/`: CI/CD unittests.
- `data/`: Raw and processed financial inclusion data.
- `notebooks/`: Task-specific analysis (Exploration, EDA).
- `src/`: Reusable Python modules (data_loader.py).
- `reports/`: Interim reports and visualization figures.
- `data_enrichment_log.md`: Detailed log of external data sources.

## Key Insights
1. **Growth Stagnation:** Account ownership growth slowed to +3pp in the 2021-2024 period.
2. **Access-Usage Gap:** High registered account counts do not yet equate to high unique adult ownership.
3. **Digital Intensity:** Existing users are shifting heavily from cash to P2P digital transfers.

## How to Run
1. Clone the repository.
2. Create a virtual environment: `python -m venv .venv`
3. Activate environment: `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run notebooks in the `notebooks/` folder.