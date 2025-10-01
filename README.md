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
├── images/                    # Скриншоты и изображения для README
│   └── screenshot_head10.png
│
├── data_loader.py             # Скрипт для загрузки и первичной обработки датасета
├── environment.yml            # Конфигурация conda окружения
├── pyproject.toml             # Файл проекта Poetry с зависимостями
├── poetry.lock                # Зафиксированные версии зависимостей
├── .gitignore                 # Файл игнорирования (содержит строку "data/")
└── README.md                  # Документация проекта

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

## Запуск скрипта проекта

1. **Запустить скрипт для чтения датасета:**
```powershell
poetry run python data_loader.py
```


Данный скрипт выполняет следующие действия:
1) Загружает исходный датасет с Google Диска (по переменной окружения FILE_ID)
2) Преобразует столбец Class в категориальный тип (category)
3) Остальные столбцы оставляет без изменений (210 колонок float64, 382 колонки int64, 3 колонки object: CID, mol, Model)
4) Сохраняет обработанный датасет в формате Parquet (data/processed_dataset.parquet)
5) Выводит информацию о датафрейме (info()) и первые 10 строк (head(10))

Этот скрипт служит для первичной загрузки, типизации и сохранения датасета для последующей обработки и анализа.

**Вывод скрипта** 

![Dataset head](images/screenshot_head10.png)
