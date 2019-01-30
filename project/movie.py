import json
import csv
import os
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# 토큰 설정 및 url 불러오기
token = os.getenv("API_TOKEN")
listt = []

# csv에 작성
with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('movie_code', 'movie_name_ko','movie_name_en', 'movie_name_og', 'prdt_year', 'genres', 'directors', 'watch_grade_nm', 'actor1', 'actor2', 'actor3')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    movie_code = boxofficelist["boxOfficeResult"]["weeklyBoxOfficeList"][i]["movieCd"]


    




    # csv 저장
with open('movie.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip().split(','))