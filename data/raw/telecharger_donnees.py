"""Télécharge les 4 séries FRED utilisées dans le projet F3 (exécuter depuis la racine du dépôt)."""
import datetime, os
import pandas as pd

SERIES = ["CPIAUCSL", "UNRATE", "FEDFUNDS", "MCOILWTICO"]
os.makedirs("data/raw", exist_ok=True)
for sid in SERIES:
    pd.read_csv(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}").to_csv(f"data/raw/{sid}.csv", index=False)
    print("OK", sid)
open("data/raw/date_extraction.txt", "w").write(str(datetime.date.today()))
