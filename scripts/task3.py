import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / "data"
OUT_DIR = BASE / "output"

pt_df = pd.read_parquet(DATA_DIR / "pr_task_type.parquet")

task3 = pt_df[["id", "title", "reason", "type", "confidence"]].copy()

task3.columns = ["PRID", "PRTITLE", "PRREASON", "PRTYPE", "CONFIDENCE"]

task3.to_csv(OUT_DIR / "pr_task_type.csv", index=False)
