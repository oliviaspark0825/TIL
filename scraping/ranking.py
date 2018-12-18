
import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
req = requests.get(url).text
soup = BeautifulSoup(req, )
