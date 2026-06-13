import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# REMOVE o seed fixo
# np.random.seed(42)

n = 3000

base = datetime.now()

logs = []

for i in range(n):

    hora = base + timedelta(seconds=i * 60)

    requests = np.random.randint(1, 120)

    status = np.random.choice(
        [200, 200, 200, 200, 401, 403, 429, 500]
    )

    logs.append([
        hora,
        f"192.168.1.{np.random.randint(1,255)}",
        np.random.choice([
            "/login",
            "/api/user",
            "/transfer",
            "/payment",
            "/pix",
            "/saldo"
        ]),
        requests,
        status
    ])

# quantidade aleatória de ataques
ataques = np.random.randint(10, 120)

for _ in range(ataques):

    logs.append([
        base,
        f"10.0.0.{np.random.randint(1,50)}",
        np.random.choice([
            "/login",
            "/transfer",
            "/payment"
        ]),
        np.random.randint(500,7000),
        np.random.choice([
            401,
            403,
            429
        ])
    ])

df = pd.DataFrame(
    logs,
    columns=[
        "timestamp",
        "ip",
        "endpoint",
        "requests",
        "status"
    ]
)

df.to_csv(
    "data/api_logs.csv",
    index=False
)

print(f"Logs gerados. Ataques simulados: {ataques}")