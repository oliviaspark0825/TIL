from time import sleep

def sleep_3s():
    sleep(3)
    print('wake up!')

print('start sleeping')
sleep_3s()
print('end of program') # 저 함수가 뒤에 호출될 프린트를 막아버림