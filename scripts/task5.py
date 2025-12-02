import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / "output"
OUT_DIR = BASE / "output"

task1_df = pd.read_csv(DATA_DIR / "all_pull_request.csv")
task3_df = pd.read_csv(DATA_DIR / "pr_task_type.csv")

merged = task1_df.merge(
        task3_df,
        left_on = "ID",
        right_on = "PRID",
        how = "left"
)

security_keywords = [
    "security",
    "vulnerability",
    "xss",
    "csrf",
    "buffer overflow",
    "sanitize",
    "encryption",
    "decrypt",
    "authentication",
    "authorization",
    "sql injection",
]

def is_security_pr(title, body):
    text = f"{title} {body}".lower()
    return int(any(keyword in text for keyword in security_keywords))

merged["SECURITY"] = merged.apply(
        lambda row: is_security_pr(row["TITLE"], row["BODYSTRING"]),
        axis = 1
)


final = merged[["ID", "AGENTNAME", "PRTYPE", "CONFIDENCE", "SECURITY"]].copy()

final.columns = ["ID", "AGENT", "TYPE", "CONFIDENCE", "SECURITY"]

final.to_csv(OUT_DIR / "task5_final.csv", index=False)
