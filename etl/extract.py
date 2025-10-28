import pandas as pd
import os

def extract_data(file_id: str, output_dir: str = 'data/raw') -> pd.DataFrame:
    file_url = f'https://drive.google.com/uc?id={file_id}'
    df = pd.read_csv(file_url)
    if df.empty:
        raise ValueError('CSV пустой!')
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, 'raw_data.csv'), index=False)
    print(f'Сырые данные сохранены в {output_dir}/raw_data.csv')
    return df
