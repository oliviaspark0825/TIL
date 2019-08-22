다른사람 git branch < release>를 불러와서 pull 하고 싶을때

---- release로 이동

git remote set-branches --add origin release

git fetch origin release:release

---- 해당 브랜치(release)로 이동

git checkout release

git branch



git push origin new



다른 브랜치를 불러와서

 git checkout -t origin/uiux
Switched to a new branch 'uiux'

다 합친거 불러올때

git pull origin create_review