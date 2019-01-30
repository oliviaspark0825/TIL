import requests
import json
import csv
import os
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

#1번문제

# 주간 시간 설정 방법
time = datetime(2019, 1, 13)
timebyweek= time.strftime("%Y%m%d")

# 토큰 설정 및 url 불러오기
token = os.getenv("API_TOKEN")
movielist = []

# csv에 작성
with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('movie_code', 'title', 'audience', 'date')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    #10주를 돌리겠다
    for s in range(10):
        url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={token}&targetDt={timebyweek}&weekGb=0&itemPerPage=10'
        req = requests.get(url).json()
        #일단 오늘의 리스트에서 10개의 리스트를 뽑아오겠다
        for i in range(10):
            movie_code = req["boxOfficeResult"]["weeklyBoxOfficeList"][i]["movieCd"]
            title = req["boxOfficeResult"]["weeklyBoxOfficeList"][i]["movieNm"]
            audience = req["boxOfficeResult"]["weeklyBoxOfficeList"][i]["audiAcc"]
            date = timebyweek
            # 중복 방지를 위해서 , 기존에 등록된 영화코드가 아니면 추가
            if movie_code not in movielist:
                writer.writerow({'movie_code': movie_code, 'title': title, 'audience': audience, 'date': date})
                movielist.append(movie_code)
    # 시간을 7일씩 줄여나가면서 계속 for 문을 돌리기
        time = time + timedelta(days=- 7)
        timebyweek = time.strftime("%Y%m%d")

# csv 저장
with open('boxoffice.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip().split(','))




#2 영화진흥위원회 오픈 API
with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('movie_code', 'movie_name_ko','movie_name_en', 'movie_name_og', 'prdt_year', 'genres', 'directors', 'watch_grade_nm', 'actor1', 'actor2', 'actor3')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

 # 1번에서 뽑은 movielist 내에서 for 문을 돌리겠다
    for k in range(len(movielist)):
        url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={token}&movieCd={movielist[k]}'
        movieinfo = requests.get(url).json()

        m_code = movieinfo["movieInfoResult"]["movieInfo"]["movieCd"]
        m_n_ko = movieinfo["movieInfoResult"]["movieInfo"]["movieNm"]
        m_n_en = movieinfo["movieInfoResult"]["movieInfo"]["movieNmEn"]
        m_n_og = movieinfo["movieInfoResult"]["movieInfo"]["movieNmOg"]
        prdt_year = movieinfo["movieInfoResult"]["movieInfo"]["prdtYear"]
        genres = movieinfo["movieInfoResult"]["movieInfo"]["genres"][0]["genreNm"]
        directors = movieinfo["movieInfoResult"]["movieInfo"]["directors"][0]["peopleNm"]
        watch_grade_nm = movieinfo["movieInfoResult"]["movieInfo"]["audits"][0]["watchGradeNm"]
        actors = movieinfo["movieInfoResult"]["movieInfo"]["actors"]

        # 일단 actor 전체리스트를 불러온 다음에 , 각각의 len에 따라 빈 것을 채워주기
        if len(actors)<3:
            if len(actors) == 0:
                actor1 = ''
                actor2 = ''
                actor3 = ''
            
            if len(actors) == 1:
                actor1 = actors[0]["peopleNm"]
                actor2 = ''
                actor3 = ''
            
            if len(actors) == 2:
                actor1 = actors[0]["peopleNm"]
                actor2 = actors[1]["peopleNm"]
                actor3 = ''
        # 일단 actor가 3명 다 채워져 있는 경우
        else:
             actor1 = actors[0]["peopleNm"]
             actor2 = actors[1]["peopleNm"]
             actor3 = actors[2]["peopleNm"]

        writer.writerow({'movie_code': m_code, 'movie_name_ko': m_n_ko, 'movie_name_en': m_n_en, 'movie_name_og': m_n_og, 'prdt_year': prdt_year, 'genres': genres, 'directors': directors, 'watch_grade_nm': watch_grade_nm, 
        'actor1': actor1 , 'actor2': actor2, 'actor3': actor3 })


    # csv 저장
with open('movie.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip().split(','))
        
