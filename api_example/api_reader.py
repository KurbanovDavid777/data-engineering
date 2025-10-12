import requests
import pandas as pd
import os

# URL API HackerNews
url = "https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty"

try:
    # Пытаемся сделать запрос
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # выбросит исключение, если код ответа не 200

    # Пробуем преобразовать ответ в JSON
    data = response.json()

    # Проверим, что данные действительно в виде словаря
    if not isinstance(data, dict):
        raise ValueError("Некорректный формат данных (ожидался JSON-объект)")

    # Конвертируем в DataFrame
    df = pd.DataFrame([data])

    df.to_csv("../data/hackernews_post.csv", index=False, encoding="utf-8-sig")

    print("Данные успешно получены и сохранены:")
    print(df.head())

except requests.exceptions.Timeout:
    print("Ошибка: время ожидания запроса истекло.")
except requests.exceptions.ConnectionError:
    print("Ошибка: не удалось подключиться к серверу.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP ошибка: {e}")
except ValueError as e:
    print(f"Ошибка обработки данных: {e}")
except Exception as e:
    print(f"Непредвиденная ошибка: {e}")

