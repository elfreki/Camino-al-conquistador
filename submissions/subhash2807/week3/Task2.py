import requests
from bs4 import BeautifulSoup
import json
import csv

url = "https://jsonplaceholder.typicode.com/posts"

content = requests.get(url)
html = BeautifulSoup(content.text,'html.parser')
data = html.get_text()
object_data = json.loads(data)

with open('data.csv','w',newline='') as f:
    fieldnames = ['id','userId','title','body']
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for x in object_data:
        writer.writerow({'id':x['id'],'userId':x['userId'],'title':x['title'],'body':x['body']})
