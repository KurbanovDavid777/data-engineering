import os
import pandas as pd
from sqlalchemy import create_engine, text

try:
    from config.db_credentials import user, password, host, port, database
except ImportError:
    user = password = host = port = database = None

def load_data(df: pd.DataFrame, table_name='kurbanov', output_dir='data/processed', to_db=True):
    # Сохраняем parquet
    os.makedirs(output_dir, exist_ok=True)
    parquet_path = os.path.join(output_dir, f'{table_name}.parquet')
    df.to_parquet(parquet_path, engine='pyarrow', index=False)
    print(f'Сохраняем в parquet: {parquet_path}')

    # Загружаем в PostgreSQL
    if to_db and all([user, password, host, port, database]):
        engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

        # Уникализируем заголовки
        headers = df.columns.tolist()
        seen = {}
        unique_headers = []
        for h in headers:
            if h in seen:
                seen[h] += 1
                unique_headers.append(f"{h}_{seen[h]}")
            else:
                seen[h] = 0
                unique_headers.append(h)

        # Подготовка данных (только первые 100 строк)
        rows = [dict(zip(unique_headers, row)) for row in df.head(100).values]

        # Определяем колонки как TEXT
        columns_def = ', '.join(f'"{col}" TEXT' for col in unique_headers)
        cols_string = ', '.join([f'"{col}"' for col in unique_headers])
        placeholders = ', '.join([f":{col}" for col in unique_headers])
        insert_query = text(f"INSERT INTO {table_name} ({cols_string}) VALUES ({placeholders})")

        with engine.begin() as conn:
            conn.execute(text(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"))
            for row in rows:
                conn.execute(insert_query, row)

        print(f'Загружено 100 строк в таблицу БД "{table_name}"')
