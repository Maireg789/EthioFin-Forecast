import streamlit as st
import pandas as pd
import os
from pathlib import Path

# --- 1. CONFIGURATION & PATHING ---
st.set_page_config(page_title="EthioFin Forecast", layout="wide", page_icon="🇪🇹")

# Robust path handling: Find images relative to this script
BASE_DIR = Path(__file__).resolve().parent.parent
FIGURES_DIR = BASE_DIR / "reports" / "figures"

def load_image(filename):
    img_path = FIGURES_DIR / filename
    if img_path.exists():
        return str(img_path)
    return None

# --- 2. SIDEBAR NAVIGATION ---
st.sidebar.image("https://img.icons8.com/fluency/96/ethiopia-map.png", width=100)
st.sidebar.title("EthioFin Forecast v1.0")
st.sidebar.markdown("Tracking Ethiopia's Digital Transformation")
page = st.sidebar.radio("Navigation", ["Strategic Overview", "Event Impact Analysis", "2027 Projections"])

# --- 3. PAGE: OVERVIEW ---
if page == "Strategic Overview":
    st.title("🇪🇹 Strategic Overview: Ethiopia's Financial Inclusion")
    st.markdown("### Selam Analytics | Interim Report Insights")

    # Key Metrics Rows
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Account Ownership", "49%", "+3pp (since 2021)")
    col2.metric("Digital Usage", "~35%", "High Growth")
    col3.metric("Telebirr Users", "54M", "2024 Actual")
    col4.metric("P2P/ATM Ratio", "1.2x", "Digital > Cash")

    st.divider()

    col_left, col_right = st.columns([1, 1])

    with col_left:
        st.subheader("The Inclusion Trajectory")
        img = load_image("usage_transformation.png")
        if img:
            st.image(img, use_column_width=True)
        else:
            st.info("💡 Analysis: The 2021-2024 slowdown shows that high registration (Telebirr) is not yet unique ownership.")

    with col_right:
        st.subheader("Key Consortium Questions")
        st.info("**Q: What drives inclusion?**\nA: Market competition (M-Pesa entry) and Digital ID (Fayda) are the strongest current drivers.")
        st.warning("**Q: Why the 3pp stagnation?**\nA: Ethiopia is hitting an 'Identity Gap' and multi-SIM behavior where one user has many accounts.")
        st.success("**Q: Is digital winning?**\nA: Yes. P2P digital transfers have officially surpassed ATM cash withdrawals for the first time.")

# --- 4. PAGE: IMPACT ANALYSIS ---
elif page == "Event Impact Analysis":
    st.title("📊 Event Impact Modeling")
    st.write("How specific milestones affect Ethiopia's Access and Usage indicators.")

    img = load_image("task3_impact_heatmap.png")
    if img:
        st.image(img, caption="Association Matrix: Impact Magnitude of Events", use_column_width=True)
    else:
        st.error("Matrix visualization not found in reports/figures/.")

    st.markdown("""
    ### Impact Logic
    - **Product Launches:** (Telebirr/M-Pesa) provide the rails for **Usage**.
    - **Policy Changes:** (Digital ID) remove friction for **Access**.
    - **Infrastructure:** (4G Expansion) acts as a multiplier for both.
    """)

# --- 5. PAGE: FORECASTS ---
elif page == "2027 Projections":
    st.title("🔮 2025-2027 Inclusion Projections")
    
    # INTERACTIVE SELECTOR
    st.subheader("Select Scenario")
    scenario = st.select_slider(
        "Move the slider to see different future outcomes:",
        options=["Pessimistic", "Base Case", "Optimistic"]
    )

    col_chart, col_text = st.columns([2, 1])

    with col_chart:
        img = load_image("inclusion_forecast_2027.png")
        if img:
            st.image(img, use_column_width=True)
        else:
            st.error("Forecast chart not found.")

    with col_text:
        if scenario == "Optimistic":
            st.success("### 🚀 Optimistic\n- **2027 Forecast: 62%**\n- Assumes Fayda ID reaches 20M adults.\n- Interoperability between banks is seamless.")
        elif scenario == "Base Case":
            st.info("### 📈 Base Case\n- **2027 Forecast: 53%**\n- Assumes steady growth.\n- Mobile money usage deepens in rural areas.")
        else:
            st.warning("### ⚠️ Pessimistic\n- **2027 Forecast: 50.5%**\n- Assumes growth plateaus.\n- High inflation slows down digital adoption.")

    st.divider()
    st.button("Download Forecast Data (CSV)")