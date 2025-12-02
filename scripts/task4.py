import pandas as pd
import re
from pathlib import Path

def clean_diff(text):
    if text is None:
        return ""
    return re.sub(r'[^\x00-\x7F]+', '', str(text))

BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / "data"
OUT_DIR = BASE / "output"

pc_df = pd.read_parquet(DATA_DIR / "pr_commit_details.parquet")

pc_df["PRDIFF"] = pc_df["patch"].apply(clean_diff)

task4 = pc_df[["pr_id", "sha", "message", "filename", "status", "additions", "deletions", "changes", "PRDIFF"]].copy()

task4.columns = ["PRID", "PRSHA", "PRCOMMITMESSAGE", "PRFILE", "PRSTATUS", "PRADDS", "PRDELSS", "PRCHANGECOUNT", "PRDIFF"]

task4.to_csv(OUT_DIR / "pr_commit_details.csv", index=False)
