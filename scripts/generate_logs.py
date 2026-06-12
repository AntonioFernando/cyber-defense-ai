import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

n = 3000

base = datetime.now()

logs = []

for i in range(n):

    hora = base + timedelta(seconds=i * 60)

    requests = np.random.randint(1, 80)

    status = np.random.choice(
        [200, 200, 200, 401, 403, 500]
    )

    logs.append([
        hora,
        f"192.168.1.{np.random.randint(1,255)}",
        np.random.choice([
            "/login",
            "/api/user",
            "/transfer",
            "/payment"
        ]),
        requests,
        status
    ])

for _ in range(30):

    logs.append([
        base,
        f"10.0.0.{np.random.randint(1,20)}",
        "/login",
        np.random.randint(1000,5000),
        401
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

print("Logs gerados.")