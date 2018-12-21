

from bs4 import BeautifulSoup
import requests

url = "http://www.op.gg/summoner/userName=%EB%B9%A8%EA%B0%84%EB%B9%84%ED%96%89%EA%B8%B0"
req = requests.get(url).text
soup = BeautifulSoup(req, 'html.parser')

#2 랭크 기록이 없는 경우
for tag in soup.select('.SummonerRatingMedium .TierRankInfo'): 
    ranking = tag.select_one('.TierRank').text
    if ranking == 'Unranked':
        @app.route("/unranked")
        def unranked():
            return render_template("unranked.html")

#1 소환사가 있고, 랭크기록이 있는 경우
    else:
    winratio = tag.select_one('.winratio').text
    @app.route("/normal")
    def normal():
        return render_template("normal.html", winratio = winratio)

#3 소환사가 존재하지 않는 경우
for tag in soup.select('.Header'): 
    noname = tag.select_one('.Title').text
    @app.route("/noname")
    def noname():
        return render_template("noname.html")









