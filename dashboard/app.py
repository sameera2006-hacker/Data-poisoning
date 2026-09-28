import streamlit as st
import pandas as pd
import sqlite3
import os

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Data Poisoning + GRC",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Data Poisoning Detection + GRC Dashboard")

st.write(
    "Controlled training-data poisoning experiment, "
    "detection analysis, model impact analysis and GRC risk management."
)

st.divider()


# ==========================================
# FILE LOCATIONS
# ==========================================

impact_file = "data/detection/model_impact_results.csv"
detection_file = "data/detection/detection_evaluation.csv"
database_file = "grc/grc_database.db"


# ==========================================
# CHECK REQUIRED FILES
# ==========================================

required_files = [
    impact_file,
    detection_file,
    database_file
]

missing_files = []

for file in required_files:

    if not os.path.exists(file):
        missing_files.append(file)

if missing_files:

    st.error("Some required project files are missing.")

    for file in missing_files:
        st.write(f"- {file}")

    st.stop()


# ==========================================
# LOAD ML RESULTS
# ==========================================

impact_df = pd.read_csv(impact_file)

detection_df = pd.read_csv(detection_file)


# ==========================================
# CONNECT TO SQLITE
# ==========================================

connection = sqlite3.connect(
    database_file
)


# Load risks directly from SQLite
risk_df = pd.read_sql_query(
    "SELECT * FROM risks",
    connection
)


# Load controls directly from SQLite
control_df = pd.read_sql_query(
    "SELECT * FROM controls",
    connection
)


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Section",
    [
        "Overview",
        "Model Impact",
        "Detection",
        "GRC Risk Register",
        "GRC Controls"
    ]
)


# ==========================================
# OVERVIEW
# ==========================================

if page == "Overview":

    st.header("📊 Project Overview")

    st.write(
        "This dashboard combines the machine-learning experiment "
        "and GRC risk-management results."
    )

    st.subheader("Project Flow")

    st.code(
        """
Training Dataset
       ↓
Data Quality Check
       ↓
Clean Baseline Model
       ↓
Controlled Poisoning
       ↓
Poisoning Detection
       ↓
Model Impact Analysis
       ↓
Risk Assessment
       ↓
GRC Controls
       ↓
SQLite Database
       ↓
Streamlit Dashboard
        """
    )

    st.subheader("Key Results")

    col1, col2, col3, col4 = st.columns(4)

    # Clean baseline accuracy
    clean_accuracy = 0.8842

    # 10% poisoned accuracy
    poisoned_accuracy = impact_df.iloc[-1]["Accuracy"]

    col1.metric(
        "Clean Accuracy",
        f"{clean_accuracy * 100:.2f}%"
    )

    col2.metric(
        "10% Poisoned Accuracy",
        f"{poisoned_accuracy * 100:.2f}%"
    )

    # Detection rate
    detection_rate = float(
        detection_df[
            detection_df["Metric"] == "Detection Rate"
        ]["Value"].iloc[0]
    )

    col3.metric(
        "Detection Rate",
        f"{detection_rate * 100:.2f}%"
    )

    # Critical risks
    critical_count = (
        risk_df["risk_category"] == "Critical"
    ).sum()

    col4.metric(
        "Critical Risks",
        critical_count
    )

    st.divider()

    st.subheader("Project Components")

    st.write("✅ Dataset preprocessing")
    st.write("✅ Clean baseline model")
    st.write("✅ Label poisoning simulation")
    st.write("✅ Poisoning detection")
    st.write("✅ Model impact analysis")
    st.write("✅ GRC risk assessment")
    st.write("✅ Risk register")
    st.write("✅ NIST AI RMF control mapping")
    st.write("✅ SQLite database")


# ==========================================
# MODEL IMPACT
# ==========================================

elif page == "Model Impact":

    st.header("📉 Model Impact Analysis")

    st.write(
        "Comparison of model performance under different "
        "training-data poisoning levels."
    )

    display_df = impact_df.copy()

    display_df["Poisoning Level"] = (
        display_df["Poisoning Level"].astype(str)
    )

    st.dataframe(
        display_df,
        use_container_width=True
    )

    st.subheader("Accuracy")

    chart_data = impact_df.set_index(
        "Poisoning Level"
    )["Accuracy"]

    st.bar_chart(chart_data)

    st.subheader("F1 Score")

    f1_chart = impact_df.set_index(
        "Poisoning Level"
    )["F1 Score"]

    st.line_chart(f1_chart)

    st.info(
        "The experiment shows that increasing poisoning "
        "levels were associated with decreasing test performance "
        "for this dataset, model and poisoning method."
    )


# ==========================================
# DETECTION
# ==========================================

elif page == "Detection":

    st.header("🔍 Poisoning Detection")

    precision = float(
        detection_df[
            detection_df["Metric"] == "Precision"
        ]["Value"].iloc[0]
    )

    recall = float(
        detection_df[
            detection_df["Metric"] == "Recall"
        ]["Value"].iloc[0]
    )

    f1 = float(
        detection_df[
            detection_df["Metric"] == "F1 Score"
        ]["Value"].iloc[0]
    )

    detection_rate = float(
        detection_df[
            detection_df["Metric"] == "Detection Rate"
        ]["Value"].iloc[0]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Precision",
        f"{precision * 100:.2f}%"
    )

    col2.metric(
        "Recall",
        f"{recall * 100:.2f}%"
    )

    col3.metric(
        "F1 Score",
        f"{f1 * 100:.2f}%"
    )

    col4.metric(
        "Detection Rate",
        f"{detection_rate * 100:.2f}%"
    )

    st.subheader("Detection Evaluation")

    st.dataframe(
        detection_df,
        use_container_width=True
    )

    st.warning(
        "A detection mismatch is a suspicious indicator, "
        "not proof that a record is poisoned."
    )


# ==========================================
# GRC RISK REGISTER
# ==========================================

elif page == "GRC Risk Register":

    st.header("🛡️ GRC Risk Register")

    # Count risk categories
    critical = (
        risk_df["risk_category"] == "Critical"
    ).sum()

    high = (
        risk_df["risk_category"] == "High"
    ).sum()

    moderate = (
        risk_df["risk_category"] == "Moderate"
    ).sum()

    low = (
        risk_df["risk_category"] == "Low"
    ).sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Critical",
        critical
    )

    col2.metric(
        "High",
        high
    )

    col3.metric(
        "Moderate",
        moderate
    )

    col4.metric(
        "Low",
        low
    )

    st.subheader("Risk Register")

    st.dataframe(
        risk_df,
        use_container_width=True
    )

    st.subheader("Risk Scores")

    risk_chart = risk_df.set_index(
        "risk_id"
    )["risk_score"]

    st.bar_chart(risk_chart)


# ==========================================
# GRC CONTROLS
# ==========================================

elif page == "GRC Controls":

    st.header("🔐 GRC Controls")

    implemented = (
        control_df["status"] == "Implemented"
    ).sum()

    planned = (
        control_df["status"] == "Planned"
    ).sum()

    col1, col2 = st.columns(2)

    col1.metric(
        "Implemented Controls",
        implemented
    )

    col2.metric(
        "Planned Controls",
        planned
    )

    st.subheader("Control Mapping")

    st.dataframe(
        control_df,
        use_container_width=True
    )

    st.subheader("NIST AI RMF Functions")

    st.write(
        "**Govern** — Establish policies and accountability."
    )

    st.write(
        "**Map** — Identify and understand AI risks."
    )

    st.write(
        "**Measure** — Analyze and evaluate AI risks."
    )

    st.write(
        "**Manage** — Prioritize and address AI risks."
    )

    st.info(
        "The controls in this project are mapped to NIST AI RMF "
        "functions as part of the project's GRC methodology."
    )


# ==========================================
# CLOSE DATABASE
# ==========================================

connection.close()