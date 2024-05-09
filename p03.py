import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.naver.com')
html = response.text  ## 중요 별표

soup = BeautifulSoup(html, 'html.parser')
word=soup.select_one('.ContentHeaderView-module__tab_text___IuWnG') ##여러개의 select,  select_one 는 1개ㄱ만
print(word)