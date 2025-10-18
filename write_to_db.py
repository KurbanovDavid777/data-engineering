import csv
from sqlalchemy import create_engine, text
from secrets.db_credentials import user, password, host, port, database

csv_file = r"D:\PROJECTS\Data_engineering\data\physchem_data.csv"
table_name = 'kurbanov'

# Чтение CSV 
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)

    # Уникализируем заголовки
    seen = {}
    unique_headers = []
    for h in headers:
        if h in seen:
            seen[h] += 1
            unique_headers.append(f"{h}_{seen[h]}")
        else:
            seen[h] = 0
            unique_headers.append(h)

    # Подготовка данных с новыми ключами (только первые 100 строк)
    rows = []
    for i, row in enumerate(reader):
        if i >= 100:
            break
        rows.append(dict(zip(unique_headers, row)))

# Подключение к PostgreSQL
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

# Дефиниции колонок
columns_def = ', '.join(f'"{col}" TEXT' for col in unique_headers)

# Подготовка INSERT запроса
cols_string = ', '.join([f'"{col}"' for col in unique_headers])
placeholders = ', '.join([f":{col}" for col in unique_headers])
insert_query = text(f"INSERT INTO {table_name} ({cols_string}) VALUES ({placeholders})")

with engine.begin() as conn:
    # Создание таблицы, если её ещё нет
    conn.execute(text(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})"))

    # Вставка данных построчно
    for row in rows:
        conn.execute(insert_query, row)

print(f"Данные успешно загружены в таблицу '{table_name}'")





