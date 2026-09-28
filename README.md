# 🛡️ AI Data Poisoning Detection & GRC Risk Management

## 📌 Project Overview

AI/ML models depend heavily on the quality and integrity of their training data. If an attacker intentionally modifies training data, the model may learn incorrect patterns and produce unreliable predictions.

This project demonstrates a controlled **training-data poisoning experiment** and integrates the results with **Governance, Risk, and Compliance (GRC)** practices.

The project uses the IMDb movie-review dataset, simulates label poisoning, detects suspicious records, measures model-performance impact, and maps identified risks to security controls.

> This is an academic cybersecurity experiment using a controlled public dataset. It does not target production systems or third-party AI models.

---

## 🎯 Objectives

- Understand AI training-data poisoning
- Build a clean machine-learning baseline
- Simulate controlled label poisoning
- Experiment with different poisoning levels
- Detect suspicious training records
- Measure model-performance impact
- Assess cybersecurity risks
- Create a GRC risk register
- Map risks to security controls
- Provide dashboard-based monitoring

---

## 🏗️ Project Architecture

```text
Training Dataset
       ↓
Data Quality Check
       ↓
Preprocessing
       ↓
Clean ML Model
       ↓
Controlled Data Poisoning
       ↓
Poisoning Detection
       ↓
Model Impact Analysis
       ↓
Risk Assessment
       ↓
GRC Control Mapping
       ↓
Dashboard / Monitoring
