import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv(
    "data/api_logs.csv"
)

X = df[[
    "requests",
    "status"
]]

model = IsolationForest(
    contamination=0.01,
    random_state=42
)

df["anomaly"] = model.fit_predict(X)

anomalias = df[
    df["anomaly"] == -1
]

anomalias.to_csv(
    "results/detected_incidents.csv",
    index=False
)

print(
    f"Anomalias detectadas: {len(anomalias)}"
)