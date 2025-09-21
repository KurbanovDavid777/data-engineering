# data-engineering

## Описание датасета
В проекте используется датасет `rev8020split_desc.csv` из библиотеки **DeepChem**.  
Ссылка: https://github.com/deepchem/deepchem/blob/master/datasets/rev8020split_desc.csv 

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

## Руководство по использованию

1. **Активировать окружение:**
```powershell
conda activate data-eng
```

2. **Установить зависимости через Poetry:**
```powershell 
poetry install
```

3. **Установить переменную окружения FILE_ID (только первый раз):**
```powershell 
conda env config vars set FILE_ID=1lbOez3uheggR4F7jqCHgVNfVtvucCSp4
conda activate data-eng
```

4. **Запустить скрипт для чтения датасета:**
```powershell
poetry run python data_loader.py
```

---

## Первые 10 строк даты

![Dataset head](images/screenshot_head10.png)
