import os
import time
import requests

#PATH TO YOUR DIRECTORY
os.chdir('/Users/filip-sin-mac/Desktop')

os.getcwd()
current_path = os.listdir()

file_numbers = []
file_names = []

#QUOTE URL
url = 'https://dummyjson.com/quotes/random'

response = requests.get(url)

if response.status_code == 200:

    if "quotes.1" in current_path:
        for file in current_path:
            if file.startswith("quotes."):
                file_number = file.split(".")
                file_number = file_number[1].split("'")
                file_number = int(file_number[0])
                file_numbers.append(file_number)
            else:
                continue

        highest_num = max(file_numbers) + 1

        os.mkdir(f'quotes.{highest_num}')
        time.sleep(1)
        # print()
        # print(current_path)
        # print()
        file_names.append(f'quotes.{highest_num}')
            
    else:
        os.mkdir('quotes.1')
        time.sleep(1)
        # print()
        # print(current_path)
        # print()
        file_names.append(f'quotes.1')
        highest_num = 1

    data = response.json()
    os.chdir(f'/Users/filip-sin-mac/Desktop/quotes.{highest_num}')
    with open('random_quote.txt', 'w') as f:
        f.write(data['quote'])

else:
    print("Failed to get the quotes")
    print(response)