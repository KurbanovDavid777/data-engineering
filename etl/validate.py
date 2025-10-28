def validate_df(df):
    '''Проверка DataFrame на пустоту, пропуски и количество строк'''
    if df.empty:
        raise ValueError('Дата пустая(')
    if df.isnull().sum().sum() > 0:
        print('Ахтунг!: есть пропуски в данных')
    if len(df) > 100:
        print('Дата большая, ведь у нас больше 100 строк')
    print('Валидация выполнена без проблем!')
