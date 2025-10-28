import argparse
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from etl.validate import validate_df

def main():
    parser = argparse.ArgumentParser(description='ETL pipeline')
    parser.add_argument('file_id', help='Google Drive FILE_ID для CSV')
    parser.add_argument('--no-db', action='store_true', help='Не загружать в БД')
    args = parser.parse_args()

    df = extract_data(args.file_id)
    validate_df(df)
    df = transform_data(df)
    load_data(df, to_db=not args.no_db)

if __name__ == '__main__':
    main()
