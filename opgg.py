#2 랭크 기록이 없는 경우

from bs4 import BeautifulSoup
import requests

url = "http://www.op.gg/summoner/userName=%EB%B9%A8%EA%B0%84%EB%B9%84%ED%96%89%EA%B8%B0"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

for tag in soup.select('.SummonerRatingMedium .TierRankInfo'): 
    ranking = tag.select_one('.TierRank').text
    if ranking == 'Unranked':
        @app.route("/unranked")
        def unranked():
            return render_template("unranked.html")