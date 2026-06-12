from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent.parent

dashboard = BASE / "dashboard"
dashboard.mkdir(exist_ok=True)

logs = pd.read_csv(
    BASE / "data" / "api_logs.csv"
)

inc = pd.read_csv(
    BASE / "results" / "detected_incidents.csv"
)

# gráfico 1
plt.figure(figsize=(10,6))

plt.hist(
    logs["requests"],
    bins=40
)

plt.title(
    "Distribuição de Requisições"
)

plt.xlabel(
    "Quantidade"
)

plt.ylabel(
    "Eventos"
)

plt.savefig(
    dashboard / "requests_distribution.png",
    bbox_inches="tight"
)

plt.close()

# gráfico 2
plt.figure(figsize=(10,6))

inc["status"].value_counts().plot(
    kind="bar"
)

plt.title(
    "Anomalias por Código HTTP"
)

plt.savefig(
    dashboard / "anomaly_status.png",
    bbox_inches="tight"
)

plt.close()

# gráfico 3
plt.figure(figsize=(10,6))

top = (
    inc["ip"]
    .value_counts()
    .head(10)
)

top.plot(
    kind="bar"
)

plt.title(
    "Top IPs Suspeitos"
)

plt.savefig(
    dashboard / "top_suspicious_ips.png",
    bbox_inches="tight"
)

plt.close()

print("Dashboard concluído.")