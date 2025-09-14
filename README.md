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
