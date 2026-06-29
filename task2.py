import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

dfs = []

for file in files:
    df = pd.read_csv(file)

    df = df[df["product"] == "pink morsel"]

    df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

    df["sales"] = df["price"] * df["quantity"]

    df = df[["sales", "date", "region"]]

    dfs.append(df)

final_df = pd.concat(dfs)

final_df.to_csv("formatted_output.csv", index=False)

print("Output file created successfully!")

