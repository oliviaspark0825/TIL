git branch 각자 하다가 합쳐야할 때

1> 원격 저장소에서 모든 브랜치를 불러오기

git remote set-branches --add origin sign-in-up

확인할때 : git branch -a

git fetch origin <sign-in-up>:<sign-in-up>

확인하기: git branch -r

그러면 지금 추가한 branch가 뜨게 됨

git pull 해서 가져오면 끝

git checkout -t 



git pull origin <release>