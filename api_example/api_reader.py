import requests
import pandas as pd
import os

# URL API HackerNews
url = "https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty"

# Делаем запрос
response = requests.get(url)
data = response.json()

# Конвертируем в DataFrame
df = pd.DataFrame([data])

# Создаём папку data (игнорируем в .gitignore)
os.makedirs("../data", exist_ok=True)

# Сохраняем как CSV, но не комтитим так как папка data в ..gitignore
df.to_csv("../data/hackernews_post.csv", index=False)

print(df.head())
