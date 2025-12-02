import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / "data"
OUT_DIR = BASE / "output"

pr_df = pd.read_parquet(DATA_DIR / "all_pull_request.parquet")

#Column Selection
task1 = pr_df[["title", "id", "agent", "body", "repo_id", "repo_url"]].copy()

#Rename Columns
task1.columns = ["TITLE", "ID", "AGENTNAME", "BODYSTRING", "REPOID", "REPOURL"]

#Convert to CSV
task1.to_csv(OUT_DIR / "all_pull_request.csv", index=False)

#Temporary check
print("Wrote", OUT_DIR / "all_pull_request.csv")

