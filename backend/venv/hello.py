# a = 'spartacodingclub@gmail.com'
#
# #채워야하는 함수
# def check_mail(s):
# 	if s.find('@')==None:
#         return False
#     else:
#         return True
#
# #결과값
# print(check_mail(a))
#
# #아래와 같이 출력됩니다
# True

a = 'spartacodingclub@gmail.com'

#채워야하는 함수
def get_mail(s):
	return s.split('@')[1].split('.')[0]
#결과값
print(get_mail(a))




#입력값
a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

#채워야하는 함수
def count_list(a_list):
    result = {}
    for i in a_list:
        if i in result:
            result[i] +=1
        else:
            result[i] =1
    return result
#결과값
print(count_list(a))

#로또 번호 추출
import random

def get_lotto():
    samp = range(1, 47)
    numbers = random.sample(samp, 6)
    return numbers
print(get_lotto())

#아래와 같이 출력됩니다
[4, 46, 19, 34, 39, 43]

a=range(0.1, 2.9, 0.1)
print(a)

import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
