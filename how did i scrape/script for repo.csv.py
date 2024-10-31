import csv 
import requests
TOKEN = 'my token was here'
HEADERS = {'Authorization': f'token {TOKEN}'}
#functions
checknull=lambda x:"" if(x==None) else x['key']

count=0
with open('all_users.csv','r',newline="",encoding='utf-8') as file , open('repositories.csv',"w",newline="",encoding='utf-8') as newfile:
    reader=csv.reader(file)
    writer=csv.writer(newfile)
    for row in reader:
        count+=1
        print(count)
        link=row[1]
        params={
            "per_page":100,
            "page":1
        }
        users = []

        while True:
            response=requests.get(f'{link}/repos',headers=HEADERS,params=params)
            if response.status_code != 200:
                print("Error fetching users:", response.json())
                break
          
            data = response.json()
            repos=data

            print(f"Fetched page {params['page']} ")
            if params['page']==6:
                print("user completed")
                break
            if 'next' in response.links:
                params['page'] += 1
                print(".", end="", flush=True)
            else:
                print("\nNo more pages.")
                break
        #now write the fetched info in the file
        #iterator is repo
        for repo in repos:
            login=repo['owner']['login']
            full_name=repo['full_name']
            created_at=repo['created_at']
            stargazers_count=repo['stargazers_count']
            watchers_count=repo['watchers_count']
            language=repo['language']
            has_projects=repo['has_projects']
            has_wiki=repo['has_wiki']
            license_name=checknull(repo['license'])     

            writer.writerow([login,full_name,created_at,stargazers_count,watchers_count,language,has_projects,has_wiki,license_name])   
