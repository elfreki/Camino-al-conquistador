import requests
from bs4 import BeautifulSoup
import json

url = "https://jsonplaceholder.typicode.com/comments"

data = requests.get(url)
soup = BeautifulSoup(data.text,'html.parser')
object_data = json.loads(soup.get_text())

unique = []
i=0
for dat in object_data:
    i+=1
    email = dat['email']
    if email in unique:
        print(i,"present",email)
    else:
        unique.append(email)

print(unique)