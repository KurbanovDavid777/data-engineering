import pandas as pd
import os

FILE_ID = os.getenv("FILE_ID")
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

df = pd.read_csv(file_url)

#делаем Class - категорией 
df["Class"] = df["Class"].astype("category")

#остальные оставляем как есть, тк 210 колонок float64, 382 колонки int64, 3 колонки object (CID, mol, model)

#Сохраняем в Parquet
os.makedirs("data", exist_ok=True)
df.to_parquet("data/processed_dataset.parquet", engine="pyarrow", index=False)

print(df.info())
print(df.head(10))
