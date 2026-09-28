print("========================================")
print("          GRC RISK ASSESSMENT")
print("========================================")


# Risk calculation function
def calculate_risk(likelihood, impact):

    score = likelihood * impact

    if score <= 4:
        category = "Low"

    elif score <= 9:
        category = "Moderate"

    elif score <= 16:
        category = "High"

    else:
        category = "Critical"

    return score, category


# ========================================
# RISK 1
# ========================================

risk1_score, risk1_category = calculate_risk(
    4,
    5
)


# ========================================
# RISK 2
# ========================================

risk2_score, risk2_category = calculate_risk(
    4,
    4
)


# ========================================
# RISK 3
# ========================================

risk3_score, risk3_category = calculate_risk(
    3,
    4
)


# ========================================
# RISK 4
# ========================================

risk4_score, risk4_category = calculate_risk(
    4,
    3
)


# ========================================
# DISPLAY RESULTS
# ========================================

print("\n========================================")
print("             RISK RESULTS")
print("========================================")

print("\nRISK-001")
print("Risk: Training data integrity compromise")
print("Likelihood:", 4)
print("Impact:", 5)
print("Risk Score:", risk1_score)
print("Category:", risk1_category)

print("\nRISK-002")
print("Risk: Incorrect training labels")
print("Likelihood:", 4)
print("Impact:", 4)
print("Risk Score:", risk2_score)
print("Category:", risk2_category)

print("\nRISK-003")
print("Risk: Model performance degradation")
print("Likelihood:", 3)
print("Impact:", 4)
print("Risk Score:", risk3_score)
print("Category:", risk3_category)

print("\nRISK-004")
print("Risk: False positive detection")
print("Likelihood:", 4)
print("Impact:", 3)
print("Risk Score:", risk4_score)
print("Category:", risk4_category)


print("\n========================================")
print("       DAY 18 COMPLETED")
print("========================================")