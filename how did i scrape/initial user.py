import requests
import csv

TOKEN = 'my token was here'
HEADERS = {'AUTHORISATION': f'token {TOKEN}'}

search_url = "https://api.github.com/search/users"
params = {
    'q': 'location:Basel followers:>10',
    'per_page': 100,
    'page': 1
}

users = []

while True:
    response = requests.get(search_url, headers=HEADERS, params=params)
    if response.status_code != 200:
        print("Error fetching users:", response.json())
        break
    
    data = response.json()
    users.extend(data.get('items', []))

    print(f"Fetched page {params['page']} with {len(data.get('items', []))} users.")

    if 'next' in response.links:
        params['page'] += 1
        print(".", end="", flush=True)
    else:
        print("\nNo more pages.")
        break

with open('users.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'Profile URL'])

    for user in users:
        username = user['login']
        profile_url = user['html_url']
        writer.writerow([username, profile_url])

print("\nUsers have been saved to users.csv")
