import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATA_DIR = BASE / "data"
OUT_DIR = BASE / "output"

ar_df = pd.read_parquet(DATA_DIR / "all_repository.parquet")
task2 = ar_df[["id", "language", "stars", "url"]].copy()

task2.columns = ["REPOID", "LANG", "STARS", "REPOURL"]

task2.to_csv(OUT_DIR / "all_repository.csv", index=False)



