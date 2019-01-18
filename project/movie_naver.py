import requests
import json
import csv
import os
from bs4 import BeautifulSoup


with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('rep_code', 'thumbnail_url','hypertext_link', 'ratings')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

for i in range(len()):
