import json

# Wczytanie danych z pliku products.json
with open('products.json', 'r') as file:
    products = json.load(file)

# Obliczanie łącznej wartości produktów w każdej kategorii
category_summary = {}

for product in products:
    category = product['kategoria']
    price = product['cena']
    quantity = product['ilosc']

    total_value = price * quantity
    if category in category_summary:
        category_summary[category] += total_value
    else:
        category_summary[category] = total_value

# Zapis wyników do pliku category_summary.json
with open('category_summary.json', 'w') as summary_file:
    json.dump(category_summary, summary_file, indent=4, ensure_ascii=False)

print("Wyniki zostały zapisane do pliku 'category_summary.json'.")
