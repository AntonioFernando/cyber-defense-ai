import pandas as pd

inc = pd.read_csv(
    "results/detected_incidents.csv"
)

with open(
    "results/response_log.txt",
    "w",
    encoding="utf-8"
) as f:

    for _, row in inc.iterrows():

        f.write(
            f"Bloqueado IP {row['ip']}\n"
        )

print(
    "Resposta automatizada concluída."
)