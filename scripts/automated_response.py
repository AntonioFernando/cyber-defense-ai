import pandas as pd
from datetime import datetime
import numpy as np

# =========================
# CARREGAR DADOS
# =========================
df = pd.read_csv("results/detected_incidents.csv")

anomalies = df[df["anomaly"] == -1].copy()

# =========================
# FUNÇÃO DE SEVERIDADE
# =========================
def classify_severity(row):
    if row["status"] in [401, 403]:
        return "HIGH"
    elif row["status"] == 429:
        return "MEDIUM"
    else:
        return "LOW"

# =========================
# RESPOSTA SOAR
# =========================
actions = []

for _, row in anomalies.iterrows():

    severity = classify_severity(row)

    ip = row["ip"]
    endpoint = row["endpoint"]

    if severity == "HIGH":
        action = f"[BLOCKED] IP {ip} bloqueado por ataque em {endpoint}"
    elif severity == "MEDIUM":
        action = f"[RATE LIMIT] IP {ip} limitado em {endpoint}"
    else:
        action = f"[MONITOR] IP {ip} em observação em {endpoint}"

    actions.append(action)

# =========================
# LOG DE RESPOSTA
# =========================
with open("results/response_log.txt", "w", encoding="utf-8") as f:
    f.write(f"SOAR RESPONSE LOG - {datetime.now()}\n\n")
    for a in actions:
        f.write(a + "\n")

print(f"SOAR executado. Ações geradas: {len(actions)}")

# =========================
# INCIDENT TIMELINE (SIEM+SOAR)
# =========================
timeline = []

for _, row in anomalies.iterrows():
    timeline.append([
        row["timestamp"],
        row["ip"],
        row["endpoint"],
        row["status"],
        classify_severity(row)
    ])

df_timeline = pd.DataFrame(
    timeline,
    columns=["timestamp", "ip", "endpoint", "status", "severity"]
)

df_timeline.to_csv(
    "results/incident_timeline.csv",
    index=False
)

# =========================
# MTTR (SIMULADO)
# =========================
df_timeline["mttr_seconds"] = np.random.randint(
    1, 8, len(df_timeline)
)

avg_mttr = np.mean(df_timeline["mttr_seconds"])

print(f"MTTR médio: {avg_mttr:.2f} segundos")