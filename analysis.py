import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test

file_name = "data/egfr_survival.csv"

df = pd.read_csv(file_name)

# Keep the columns needed for the survival analysis
df = df[["PATIENT_ID", "OS_MONTHS", "OS_STATUS", "EGFR_STATUS"]].copy()

# Remove rows where the required information is missing
df = df.dropna()

# Convert survival time to numbers
df["OS_MONTHS"] = pd.to_numeric(df["OS_MONTHS"], errors="coerce")

# cBioPortal commonly stores OS status as "0:LIVING" or "1:DECEASED".
# This converts it into a simple 0/1 event column.
def make_event(value):
    value = str(value).upper()

    if "DECEASED" in value or value.startswith("1"):
        return 1

    if "LIVING" in value or value.startswith("0"):
        return 0

    return None


df["event"] = df["OS_STATUS"].apply(make_event)
df = df.dropna(subset=["OS_MONTHS", "event"])

df["event"] = df["event"].astype(int)

altered = df[df["EGFR_STATUS"].str.lower() == "altered"]
unaltered = df[df["EGFR_STATUS"].str.lower() == "unaltered"]

print("Total patients:", len(df))
print("EGFR altered:", len(altered))
print("EGFR unaltered:", len(unaltered))

# Kaplan-Meier curves
kmf_altered = KaplanMeierFitter()
kmf_unaltered = KaplanMeierFitter()

kmf_altered.fit(
    altered["OS_MONTHS"],
    event_observed=altered["event"],
    label="EGFR-Altered"
)

kmf_unaltered.fit(
    unaltered["OS_MONTHS"],
    event_observed=unaltered["event"],
    label="EGFR-Unaltered"
)

plt.figure(figsize=(8, 6))

kmf_altered.plot(ci_show=True)
kmf_unaltered.plot(ci_show=True)

plt.title("TCGA-LUAD Overall Survival: EGFR Altered vs Unaltered")
plt.xlabel("Time (Months)")
plt.ylabel("Overall Survival Probability")
plt.grid(alpha=0.25)
plt.tight_layout()

plt.savefig("results/kaplan_meier_egfr.png", dpi=300)
plt.close()

# Log-rank test
test = logrank_test(
    altered["OS_MONTHS"],
    unaltered["OS_MONTHS"],
    event_observed_A=altered["event"],
    event_observed_B=unaltered["event"]
)

print("Log-rank p-value:", test.p_value)

# Write a small text summary
with open("results/summary.txt", "w", encoding="utf-8") as f:
    f.write("EGFR survival analysis\n")
    f.write("=====================\n\n")
    f.write(f"Total patients: {len(df)}\n")
    f.write(f"EGFR altered: {len(altered)}\n")
    f.write(f"EGFR unaltered: {len(unaltered)}\n")
    f.write(f"Log-rank p-value: {test.p_value:.6g}\n")

    altered_median = kmf_altered.median_survival_time_
    unaltered_median = kmf_unaltered.median_survival_time_

    f.write(f"Median survival, EGFR altered: {altered_median}\n")
    f.write(f"Median survival, EGFR unaltered: {unaltered_median}\n")

print("\nAnalysis finished.")
print("Plot saved to results/kaplan_meier_egfr.png")
print("Summary saved to results/summary.txt")
