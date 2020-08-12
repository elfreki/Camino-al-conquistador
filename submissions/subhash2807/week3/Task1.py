import requests
from bs4 import BeautifulSoup
url="http://www.mocky.io/v2/5b026eb43000007a00cee110"
content = requests.get(url)
print("flag:",content.headers['flag'])
print("headers:",content.headers)
