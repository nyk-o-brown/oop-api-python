import requests
from tabulate import tabulate


response = requests.get("https://api.thecatapi.com/v1/breeds")

breeds_data = response.json()

table_data = []
for breed in breeds_data:
    table_data.append([
        breed['name'],
        breed['origin'],
        breed['temperament'],  # Fixed spelling here
        breed['description'][:50]
        
        
    ])
headers = ['Breed Name', 'Origin', 'Temperament', 'Description']  # Fixed spelling here


print(tabulate(table_data, headers=headers, tablefmt='grid'))