import csv
import requests
import csv 
# Open the CSV file
#functions
companyfunction=lambda x: "" if(x == None) else x
lengthfunc=lambda x:"" if(len(x)<2) else x[1]

TOKEN = 'here my token was there'
HEADERS = {'Authorization': f'token {TOKEN}'}
count=0
with open('all_users.csv', mode='r', newline='', encoding='utf-8') as file, open('users.csv',mode='w',newline='', encoding='utf-8') as newfile:
    reader = csv.reader(file)
    # Iterate through each row in the CSV file
    for row in reader:
        link = row[1]  # Second column
        
        response=requests.get(f'{link}',headers=HEADERS)
        if response.status_code != 200:
            print("Error fetching users:", response.json())
            break
        data=response.json()
        login=data['login']
        name=data['name']
       
        tempcompany=companyfunction(data['company']).strip()#function called 
        tempcompany2=tempcompany.strip('@')
        company=tempcompany2.upper()#exception can occur here
        location=data['location']
        email=data['email']
        hireable=data['hireable']
        bio=data['bio']
        public_repos=data['public_repos']
        followers=data['followers']
        following=data['following']
        created_at=data['created_at']


        writer=csv.writer(newfile)
        writer.writerow([login,name,company,location,email,hireable,bio,public_repos,followers,following,created_at]) 
        count+=1
        print(count)







        
