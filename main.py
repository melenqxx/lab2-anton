import csv
import random
import xml.etree.ElementTree as ET

with open("books.csv", encoding="cp1251") as f:
    books = list(csv.DictReader(f, delimiter=";"))

# год лежит в дате поступления: "15.10.2021 9:22" -> символы с 6 по 10
for b in books:
    b["Год"] = int(b["Дата поступления"][6:10])

# 1
count = 0
for b in books:
    if len(b["Название"]) > 30:
        count += 1
print("Книг с названием длиннее 30 символов:", count)
input("\nНажми Enter, чтобы идти дальше...\n")

# 2
name = input("Какого автора ищем? ").lower()
found = False
for b in books:
    if name in b["Автор"].lower() and b["Год"] < 2016:
        print(b["Автор"], "-", b["Название"], "-", b["Год"])
        found = True
if not found:
    print("Ничего не нашлось")
input("\nНажми Enter, чтобы идти дальше...\n")

# 3
with open("refs.txt", "w", encoding="utf-8") as out:
    for i, b in enumerate(random.sample(books, 20), 1):
        out.write(f"{i}. {b['Автор']}. {b['Название']} - {b['Год']}\n")
print("Готово, ссылки лежат в refs.txt")
input("\nНажми Enter, чтобы идти дальше...\n")

# 4. Валюты из xml: два списка
names = []
values = []
for v in ET.parse("currency.xml").getroot().findall("Valute"):
    names.append(v.find("Name").text)
    values.append(float(v.find("Value").text.replace(",", ".")))
print(names)
print(values)
input("\nНажми Enter, чтобы идти дальше...\n")

# Допзадание 
tags = set()
for b in books:
    for tag in b["Жанр книги"].split("#"):
        if tag.strip() != "":
            tags.add(tag.strip())
print("Всего разных тегов:", len(tags))
print(sorted(tags))
input("\nНажми Enter, чтобы идти дальше...\n")

# Допзадание 2. Топ-20 по количеству выдач (суммируем по названию)
popular = {}
for b in books:
    title = b["Название"]
    popular[title] = popular.get(title, 0) + int(b["Кол-во выдач"])
top = sorted(popular.items(), key=lambda x: x[1], reverse=True)[:20]
for i, (title, n) in enumerate(top, 1):
    print(i, title, "-", n)