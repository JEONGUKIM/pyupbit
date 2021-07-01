# 1. while 문을 사용하여 10,000 원에서 5일연속 상한가(30%)를 기록한 경우의 금액을 출력하세요.

money = 10000
# day = 1
#
# while day < 6 :
#     money = money * 1.3
#     print(day, money)
#     day += 1
# print("최종:", money)


# 2. 로또번호 1-45의 숫자 6개를 생성해보세요. (숫자중복없음) /

# import random
#
# lotto = []
# while len(lotto) < 6:
#     numbers = random.randint(1, 45)
#     if numbers not in lotto:
#         lotto.append(numbers)
# print(lotto)


################ 복     습 #########################
# 001
# print("Hello World")

# 002
# print("Mary's cosmetics")

# 003
# print('신씨가 소리질렀다. "도둑이야".')

# 004
# print("C:\windows")

# 005
# print("안녕하세요\n만나서\t\t반갑습니다.")

# 006
# print("오늘은", "일요일")

# 007  !!
# print("naver", "kakao", "samsung", sep=";")

# 008
# print("naver", "kakao", "sk", "samsung", sep="/")

# 009
# print("first", end=" "); print("second")

# 010
# print(5/3)

# 011
# 삼성전자 = 50000
# 평가금액 = 삼성전자 * 10
# print("총평가금액: {:,}".format(평가금액))

# 012
# 시가총액 = 298000000000000
# 현재가 = 50000
# PER = 15.19
# print(시가총액, type(시가총액))
# print(현재가, type(현재가))
# print(PER, type(PER))

# 013
# s = "hello"
# t = "python"
# print(s + "!", t)

# 014
# print(2 + 2 *3)

# 015
# a = "132"
# print(type(a))

# 016
# num_str = "720"
# num_int = int(num_str)
# print(num_int+1, type(num_int))

# 017
# num = 100
# num_str = str(num)
# print(num_str, type(num_str))

# 018
# a = "15.79"
# a_float = float(a)
# print(a_float, type(a_float))

# 019
# year = "2020"
# year = int(year)
# for i in range(3):
#     print(year + (i - 3))

# 020
# 월 = 48584
# 총금액 = 월 * 36
# print(총금액)

# 021
# letters = 'python'
# print(letters[0], letters[2])

# 022
# license_plate = "24가 2210"
# license_plate = license_plate.split()
# print(license_plate[1])

# 023
# string = "홀짝홀짝홀짝"
# print(string[::2])

# 024
# string = "PYTHON"
# print(string[::-1])

# 025
# phone_number = "010-1111-2222"
# print(phone_number.replace("-", " "))

# 026
# phone_number = "010-1111-2222"
# print(phone_number.replace("-", ""))

# 027
# url = "http://sharebook.kr"
# print(url.split(".")[1])

# 028
# lang = 'python'
# lang[0] = 'P'
# print(lang)

# 029
# string = 'abcdfe2a354a32a'
# string = string.replace("a", "A")
# print(string)

# 030
# string = 'abcd'
# string.replace('b', 'B')
# print(string)

# 031
# a = "3"
# b = "4"
# print(a + b)

# 032
# print("Hi" * 3)

# 033
# print("-" * 80)

# 034   !!
# t1 = 'python'
# t2 = 'java'
# t3 = t1 + ' ' + t2 + ' '
# print(t3 * 4)

# 035
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
#
# print("이름: %s 나이: %d" %(name1, age1))
# print("이름: %s 나이: %d" %(name2, age2))

# 036
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
#
# print("이름: {} 나이: {}".format(name1, age1))
# print("이름: {} 나이: {}".format(name2, age2))

# 037
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
#
# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")

# 038
# 상장주식수 = "5,969,782,550"
# 상장주식수 = 상장주식수.replace(",", "")
# 상장주식수 = int(상장주식수)
# print(상장주식수, type(상장주식수))

# 039
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])

# 040       !!
# data = "   삼성전자    "
# data = data.strip()
# print(data)

# 041
# ticker = "btc_krw"
# print(ticker.upper())

# 042
# ticker = "BTC_KRW"
# print(ticker.lower())

# 043
# a = "hello"
# print(a.capitalize())

# 044   !!
# file_name = "보고서.xlsx"
# print(file_name.endswith("xlsx"))

# 045  !!
# file_name = "보고서.xlsx"
# print(file_name.endswith(("xlsx", "xls",)))

# 046
# file_name = "2020_보고서.xlsx"
# print(file_name.startswith("2020"))

# 047
# a = "hello world"
# a = a.split()
# print(a)

# 048
# ticker = "btc_krw"
# ticker = ticker.split("_")
# print(ticker)

# 049
# date = "2020-05-01"
# date = date.split("-")
# print(date)

# 050
# data = "039490     "
# data = data.rstrip()
# print(data)

# 051
# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# print(movie_rank)

# 052   !!
# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("배트맨")
# print(movie_rank)

# 053   !!
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)

# 054
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# del movie_rank[3]
# print(movie_rank)

# 055
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)

# 056
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1 + lang2
# print(langs)

# 057   !!
# nums = [1, 2, 3, 4, 5, 6, 7]
# print("max:", max(nums))
# print("min:", min(nums))

# 058
# nums = [1, 2, 3, 4, 5]
# print(sum(nums))

# 059
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# 060
# nums = [1, 2, 3, 4, 5]
# print(sum(nums) / len(nums))

# 061
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])

# 062
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])
#
# list = []
# for i in nums:
#     if i % 2 != 0:
#         list.append(i)
# print(list)

# 063
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])

# 064
# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# 065
# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0], interest[2])

# 066   !!
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(" ".join(interest))

# 067
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("/".join(interest))

# 068
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("\n".join(interest))

# 069
# string = "삼성전자/LG전자/Naver"
# interest = string.split("/")
# print(interest, type(interest))

# 070   !!
# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)
#
# data = [2, 4, 3, 1, 5, 10, 9]
# data1 = sorted(data)
# print(data1)
# print(data)
#
# data2 = sorted(data, reverse= True)     # 내림차순 sort 에도 적용가능
# print(data2)

# 071
# my_variable = ()
# print(my_variable, type(my_variable))

# 072
# movie_rank = "닥터스트 레인지", "스플릿", "럭키"
# print(movie_rank, type(movie_rank))

# 073
# a = (1, )
# print(a, type(a))

# 074
# t = (1, 2, 3)
# t[0] = 'a'
#
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

# 075
# t = 1, 2, 3, 4
# print(t, type(t))

# 076
# t = ('a', 'b', 'c')
# t = ('A', 'B', "c")
# print(t)

# 077
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# interest = list(interest)
# print(interest, type(interest))

# 078
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# interest = tuple(interest)
# print(interest, type(interest))

# 079
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)

# 080   !!
# a = tuple(range(2, 100, 2))
# print(a)

# 081
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, a, b = scores
# print(valid_score)

# 082
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, b, *valid_score = scores
# print(a, b, valid_score)

# 083
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, *valid_score, b = scores
# print(a, valid_score, b)

# 084
# temp = { }
# print(temp)

# 085
# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# print(ice)
# print(ice.keys())
# print(ice.values())

# 086
# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# ice["죠스바"] = 1200
# ice["월드콘"] = 1500
# print(ice)

###  리스트: 추가(append), 끼워넣기(insert), 삭제(del) / 튜플: 수정불가 / 딕셔너리: 추가, 삭제, 업데이트(새로운 딕셔너리 변수 추가)

# 087   !!
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
#
# print("메로나 가격:", ice["메로나"])

# 088
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
#
# ice["메로나"] = 1300
# print(ice)

# 089
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
#
# del ice["메로나"]
# print(ice)

# 090
# >> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# >> icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'

# 091
# inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100] }
# print(inventory)

# 092
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
#
# print(inventory["메로나"][0], "원")

# 093
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
#
# print(inventory["메로나"][1], "개")

# 094
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
#
# inventory["월드콘"] = [500, 7]
# print(inventory)

# 095   !!
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# key_list = list(icecream.keys())
# print(key_list)

# 096
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# values_list = list(icecream.values())
# print(values_list)

# 097
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# sell = sum(icecream.values())
# print(sell)

# 098   !!
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
#
# icecream.update(new_product)
# print(icecream)

# 099   !!!!!! !! !!
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
#
# result = dict(zip(keys, vals))      ## 튜플, 리스트, 튜플+리스트, 전부 딕셔너리로 합치기 가능.
# print(result)

# 100
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
#
# close_table = dict(zip(date, close_price))
# print(close_table)
