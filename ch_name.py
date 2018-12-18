# 절대주소를 불러와야하니까 폴더에 들어가서 클릭하며 나옴 윈도우는 r을 입력해야함
import os
os. chdir(r"C:\Users\student\Desktop\TIL\dummy")
# 리스트를 데리고 와야함 // 이미 <chdir>로 위치를 이동했으니까 현재위치 = . 임 // 변수는 이름 하나 지정해주는 것임 filename 내맘대로 단, 단수를 해야함 
for filename in os.listdir("."):
    os.rename(filename, "SAMSUNG " + filename)

# 파일명을 다시 SSAFY로 바꿔야하는 상황

#import os
#os. chdir(r"C:\Users\student\Desktop\TIL\dummy")
#for filename in os.listdir("."):
 #   os.rename(filename, filename.replace("SAMSUNG ", "SSAFY"))

import os
os. chdir(r"C:\Users\student\Desktop\TIL\dummy")
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SAMSUNG SSAFY", "SSAFY"))
