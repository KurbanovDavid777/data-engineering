import pandas as pd

physchem_cols = [
    'pIC50', 'MW', 'AlogP', 'HBA', 'HBD', 'RB',
    'HeavyAtomCount', 'ChiralCenterCount', 'ChiralCenterCountAllPossible',
    'RingCount', 'PSA', 'Estate', 'MR', 'Polar'
]

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.head(100).copy()  # ограничение 100 строк
    if 'Class' in df.columns:
        df['Class'] = df['Class'].astype('category')
    df_physchem = df[[col for col in physchem_cols if col in df.columns]].copy()
    print(f'Преобразовано {df_physchem.shape[1]} колонок с физико-химическими свойствами')
    return df_physchem
