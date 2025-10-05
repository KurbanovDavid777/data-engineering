# Books to Scrape Parser

Простой скрипт для парсинга сайта [Books to Scrape](http://books.toscrape.com/).

## Описание

Скрипт загружает книги с главной страницы, извлекает:
- Название книги
- Ссылку
- Стоимость
- Наличие на складе

И сохраняет результат в CSV (`../data/books.csv`) в UTF-8, чтобы корректно отображались символы валют.

## Использование

```powershell
# Установить зависимости через poetry
poetry install

# Запустить скрипт
poetry run python data_parser.py

```
## Скриншот работы скрипта

![Вывод скрипта](.../images/books_parser_output.png)
