import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

BASE = "http://books.toscrape.com/"

# Загружаем страницу
response = requests.get(BASE)
response.encoding = "utf-8" 
soup = BeautifulSoup(response.text, "html.parser")

# Ищем все книги
books = soup.find_all("article", class_="product_pod")

# Извлекаем данные
data = []
for book in books:
    title_el = book.find("h3").find("a")
    price_el = book.find("p", class_="price_color")
    availability_el = book.find("p", class_="instock availability")
    
    title = title_el["title"]
    link = urljoin(BASE, title_el["href"])
    price = price_el.get_text(strip=True) if price_el else "Не указана"
    availability = availability_el.get_text(strip=True) if availability_el else "Не указана"
    
    data.append([title, link, price, availability])

# Создаем DataFrame и сохраняем
df = pd.DataFrame(data, columns=["Title", "Link", "Price", "Availability"])
df.to_csv("../data/books.csv", index=False, encoding="utf-8-sig")

# Выводим первые строки
print(df.head())
