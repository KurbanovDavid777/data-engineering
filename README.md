# data-engineering

## Описание датасета
В проекте используется датасет `rev8020split_desc.csv` из библиотеки **DeepChem**.  
Ссылка: https://github.com/deepchem/deepchem/blob/master/datasets/rev8020split_desc.csv 

Ссылка на гугл диск: https://drive.google.com/file/d/1lbOez3uheggR4F7jqCHgVNfVtvucCSp4/view?usp=sharing

Краткая характеристика датасета:
1) RangeIndex: 1475 entries, 0 to 1474
2) Columns: 595 entries, mol to idx
3) dtypes: float64(210), int64(382), object(3)
4) memory usage: 6.7+ MB

- Каждая строка соответствует отдельной молекуле  
- Столбцы содержат молекулярные дескрипторы (числовые признаки), а также идентификаторы (`mol`, `smiles`, `idx`)  
 
Данные подходят для:
- обработки и анализа химических данных,  
- построения ETL-процессов,  
- задач машинного обучения (регрессия/классификация).  

## Структура проекта
```

Data_engineering/
│
├── api_example/                     # Пример с API HackerNews
│   ├── api_reader.py                # Скрипт для загрузки данных из API
│   └── README.md                    # Документация к примеру API
│
├── parse_example/                   # Пример с парсингом HTML
│   ├── data_parser.py               # Скрипт для парсинга сайта books.toscrape.com
│   └── README.md                    # Документация к примеру парсинга
│
├── notebooks/                       # Ноутбуки
|   └── EDA.ipynb
|
├── .gitignore
|   └── data/ 
│   ├── config/          
│   ├── __pycache__/
│
├── images/                          # Скриншоты и изображения для README
|   ├── ETL.png                      # Скриншот вывода  ETL        
│   ├── hackernews_output.png        # Скрин вывода API-примера
│   └── books_parser_output.png      # Скрин вывода парсера
|
├── etl                             
|   ├── __init__
|   ├── extract.py                   # Загрузка сырых данных с Google Диска, базовая валидация, сохранение CSV в `data/raw/`.
|   ├── load.py                      # Сохранение обработанных данных в `data/processed/*.parquet`, а также загрузка до 100 строк в PostgreSQL (если настроена).
|   ├── main.py                      # Объединяет все этапы: загрузку, трансформацию, сохранение parquet и загрузку в БД. Требует минимум один аргумент — FILE_ID.
|   ├── transform.py                 # Преобразование данных (типизация, очистка, подготовка physchem колонок). 
|   ├── validate.py                  # Отдельные проверки валидации данных                 
|
├── pyproject.toml                   # Poetry: описание зависимостей проекта
├── poetry.lock                      # Зафиксированные версии библиотек
├── environment.yml                  # Конфигурация окружения 
├── .gitignore                       # Исключения для git (в т.ч. /data/)
└── README.md                        # Основная документация проекта


```

## Настройка проекта

1. **Клонирования репозитория:**
```powershell
git clone https://github.com/KurbanovDavid777/data-engineering.git
cd Data_engineering
```

2. **Активировать conda окружение:**
```powershell
conda create -n data-eng python=3.13 -y
conda activate data-eng
```

3. **Установить зависимости через Poetry:**
```powershell 
poetry install
poetry config virtualenvs.in-project true
```

4. **Установка необходимых библиотек через Poetry:**
```powershell 
poetry add pandas matplotlib jupyterlab wget
```

5. **Установить переменную окружения FILE_ID (только первый раз):**
```powershell 
conda env config vars set FILE_ID=1lbOez3uheggR4F7jqCHgVNfVtvucCSp4
conda deactivate
conda activate data-eng
```

## Запуск ETL пакета (новый способ)

После настройки окружения и клонирования репозитория можно запускать ETL-процесс:

```powershell
# Запуск ETL с переменной FILE_ID (ID файла на Google Диске)
# "--no-db" - означает без загрузки в базу данных SQl, чтобы запустить с выгрузкой в бд, нужно убрать "--no-db" из кода
python -m etl.main 1lbOez3uheggR4F7jqCHgVNfVtvucCSp4 --no-db
```

## Exploratory Data Analysis (EDA) датасета 

Полный интерактивный EDA ноутбук доступен для просмотра онлайн через nbviewer:

[Просмотреть EDA Notebook](https://nbviewer.org/github/KurbanovDavid777/data-engineering/blob/main/notebooks/EDA.ipynb)
