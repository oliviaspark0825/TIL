# 1파일을 만들면서 열기 write // 글 쓰고 닫기
# open close 는 항상 나옴
#f = open("new.txt", "w")
#f.write("Hello !!!")
#f.close()

#2 with 는 if 랑 같은 거고, 끝나면 자동적으로 close 해줌
#with open("new.txt", "w") as f:
  #  f.write("Ik ben moe!!!")



# 파일을 열고 내용을 가져오고 싶을 때

#f = open("new.txt", "r")
#data = f.read()
#print(data)
#f.close()

#with open("new.txt", "r") as f:
 #   data = f.read()
  #  print(data)


# 다 쓴다음에 닫아주어야 함
# for은 특정 구간 안에서 5번 돌아가라

#f = open("new.txt", "w", encoding='utf-8')
#for n in range(5):
 #   data = f"{n}번째 줄입니다.\n"
  #  f.write(data)
#f.close()

# with open("new.txt", "w", encoding='utf-8') as f:
#     for i in range(5):
#         data = f"{i}번째 줄입니다.\n"
#         f.write(data)

# menu = ["카레\n", "파스타\n", "탕수육\n"]
# f = open("menu.txt","w", encoding='utf-8')
# f.writelines(menu)
# f.close()



# with open("new.txt","w",encoding='utf-8') as f:
#     menu = ["카레\n", "파스타\n", "탕수육\n"]
#     f.writelines(menu)

#쌤코드 오후 1교시
# with open("ssafy.txt", "w", encoding='utf-8') as f:
# 	for i in range(1,11):
# 		data = f"{i}번째 줄입니다.\n"
# 		f.write(data)


# readline으로 읽기
# with open("ssafy.txt", "r", encoding='utf-8') as f:
# 	 line = f.readline()
# 	 print(line.strip())

# readlines 파일 전체를 list 형태로 리턴???
with open("ssafy.txt", "r", encoding='utf-8') as f:	 
	lines = f.readlines()
	for i in lines:
		print(i.strip())

# ANSWER # 범위를 복수로 받고, 단수로 i를 받는 것 literal  객체를 라인즈에 넣어주고, 그걸 돌려서 하나씩 출력하기
with open("ssafy.txt", "r", encoding='utf-8') as f:
	lines = f.readlines()
	for line in lines:
		print(line.strip())

