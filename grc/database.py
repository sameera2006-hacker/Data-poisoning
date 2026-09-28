import sqlite3
import pandas as pd
import os

print("========================================")
print("       GRC SQLITE DATABASE")
print("========================================")

# Database location
database_file = "grc/grc_database.db"

# Connect to SQLite database
connection = sqlite3.connect(database_file)

cursor = connection.cursor()

print("\nSQLite database connected successfully!")


# ==========================================
# CREATE RISK TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS risks (
    risk_id TEXT PRIMARY KEY,
    asset TEXT,
    threat TEXT,
    vulnerability TEXT,
    risk_description TEXT,
    likelihood INTEGER,
    impact INTEGER,
    risk_score INTEGER,
    risk_category TEXT,
    treatment TEXT,
    status TEXT
)
""")

print("Risk table created successfully!")


# ==========================================
# CREATE CONTROLS TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS controls (
    control_id TEXT PRIMARY KEY,
    risk_id TEXT,
    control TEXT,
    control_description TEXT,
    nist_ai_rmf TEXT,
    remediation TEXT,
    evidence TEXT,
    status TEXT
)
""")

print("Control table created successfully!")


# ==========================================
# LOAD RISK REGISTER
# ==========================================

risk_file = "grc/risk_register.csv"

if os.path.exists(risk_file):

    risk_df = pd.read_csv(risk_file)

    print("\nRisk register loaded:")
    print("Records:", len(risk_df))

    for _, row in risk_df.iterrows():

        cursor.execute("""
        INSERT OR REPLACE INTO risks (
            risk_id,
            asset,
            threat,
            vulnerability,
            risk_description,
            likelihood,
            impact,
            risk_score,
            risk_category,
            treatment,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["Risk ID"],
            row["Asset"],
            row["Threat"],
            row["Vulnerability"],
            row["Risk Description"],
            int(row["Likelihood"]),
            int(row["Impact"]),
            int(row["Risk Score"]),
            row["Risk Category"],
            row["Treatment"],
            row["Status"]
        ))

    print("Risk records inserted successfully!")

else:

    print("\nRisk register CSV not found!")


# ==========================================
# LOAD CONTROLS
# ==========================================

control_file = "grc/controls.csv"

if os.path.exists(control_file):

    control_df = pd.read_csv(control_file)

    print("\nControl mapping loaded:")
    print("Records:", len(control_df))

    for _, row in control_df.iterrows():

        cursor.execute("""
        INSERT OR REPLACE INTO controls (
            control_id,
            risk_id,
            control,
            control_description,
            nist_ai_rmf,
            remediation,
            evidence,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["Control ID"],
            row["Risk ID"],
            row["Control"],
            row["Control Description"],
            row["NIST AI RMF"],
            row["Remediation"],
            row["Evidence"],
            row["Status"]
        ))

    print("Control records inserted successfully!")

else:

    print("\nControls CSV not found!")


# ==========================================
# SAVE DATABASE
# ==========================================

connection.commit()

print("\nDatabase changes saved successfully!")


# ==========================================
# DISPLAY DATABASE CONTENT
# ==========================================

print("\n========================================")
print("          DATABASE CONTENT")
print("========================================")

risk_database = pd.read_sql_query(
    "SELECT * FROM risks",
    connection
)

control_database = pd.read_sql_query(
    "SELECT * FROM controls",
    connection
)

print("\nRisk Records:")
print(risk_database.to_string(index=False))

print("\nControl Records:")
print(control_database.to_string(index=False))


# ==========================================
# CLOSE DATABASE
# ==========================================

connection.close()

print("\nSQLite database connection closed.")

print("\n========================================")
print("       DAY 22 DATABASE COMPLETE")
print("========================================")

print("\nDatabase file:")
print(database_file)