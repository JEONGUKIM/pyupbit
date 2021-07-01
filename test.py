# 07, 08, 09,25, 35, 43, 44, 45, 46, 52, 53, 54, 57, 121~130


# 01
# print("Hello World")

# 02
# print("Mary's cosmetic")

# 03
# print('신씨가 소리질렀다. "도둑이야".')

# 04
# print("C:\windows")

# 05
# print("안녕하세요.\n만나서\t\t반갑습니다.")

# 06
# print("오늘은", "일요일")

# 07  !!
# print("naver", "kakao", "sk", "samsung", sep=";")

# 08  !!
# print("naver", "kakao", "sk", "samsung", sep="/")

# 09  !!
# print("first");print("second")
# print("first", end=" ");print("second")

# 10
# print(5/3)

# # 11
# 삼성전자 = 50000
# 총평가금액 = 삼성전자 * 10
# print("총평가금액:", 총평가금액)

# 12
# 시가총액 = 298000000000000
# 현재가 = 50000
# PER = 15.79
# print(시가총액, type(시가총액))
# print(현재가, type(현재가))
# print(PER, type(PER))

# 13
# s = "hello"
# t = "python"
# print(s + "!", t)

# 14
# print(2 + 2 * 3)

# 15
# a = "132"
# print(type(a))

# 16
# num_str = "720"
# print(type(num_str))
# num_int = int(num_str)
# print(type(num_int))
# print(num_int+1, type(num_int))

# 17
# num = 100
# num_str = str(num)
# print(type(num_str))

# 18
# a = "15.79"
# aa = float(a)
# print(type(aa))

# 19
# year = "2020"
# year = int(year)
# print(year - 3)
# print(year - 2)
# print(year - 1)

# 20
# 에어컨 = 48584
# 총금액 = 에어컨 * 36
# print(총금액)

# 21
# letters = 'python'
# print(letters[0], letters[2])

# 22
# license_plate = "24가 2210"
# print(license_plate[3:])
# print(license_plate[-4:])

# 23
# string = "홀짝홀짝홀짝"
# print(string[::2])

# 24
# string = "PYTHON"
# print(string[::-1])

# 25  !!
# phone_number = "010-1111-2222"
# phone_number = phone_number.replace("-", " ")
# print(phone_number)

# 26
# phone_number = "010-1111-2222"
# phone_number = phone_number.replace("-", "")
# print(phone_number)

# 27
# url = "http://sharebook.kr"
# url = url.split(".")[-1]
# print(url)

# 28
# lang = 'python'
# lang[0] = 'P'
# print(lang)

# 29
# string = 'abcdfe2a354a32a'
# A = string.replace("a", "A")
# print(A)

# 30
# string = 'abcd'
# string.replace('b', 'B')
# print(string)

# 31
# a = "3"
# b = "4"
# print(a + b)

# 32
# print("Hi" * 3)

# 33
# print("-" * 80)

# 34
# t1 = 'python'
# t2 = 'java'
# print((t1 + " " + t2+ " ") * 4)

# 35  !!
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
#
# print("이름: %s 나이: %d" % (name1, age1))
# print("이름: %s 나이: %d" % (name2, age2))

# 36
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
#
# print("이름: {} 나이: {}".format(name1, age1))
# print("이름: {} 나이: {}".format(name2, age2))

# 37
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
#
# print(f"이름: {name1} 나이:{age1}")
# print(f"이름: {name2} 나이:{age2}")

# 38
# 상장주식수 = "5,969,782,550"
# 상장주식수 = 상장주식수.replace(",", "")
# 상장주식수 = int(상장주식수)
# print(상장주식수)

# 39
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])

# 40
# data = "   삼성전자    "
# data = data.strip()
# print(data)

# 41
# ticker = "btc_krw"
# ticker = ticker.upper()
# print(ticker)

# 42
# ticker = "BTC_KRW"
# ticker = ticker.lower()
# print(ticker)

# 43  !!
# a = "hello"
# a = a.capitalize()
# print(a)

# 44  !!
# file_name = "보고서.xlsx"
# a = file_name.endswith("xlsx")
# print(a)

# 45  !!
# file_name = "보고서.xlsx"
# a = file_name.endswith(("xlsx", "xls",))
# print(a)

# 46  !!
# file_name = "2020_보고서.xlsx"
# a = file_name.startswith("2020")
# print(a)

# 47
# a = "hello world"
# a = a.split()
# print(a)

# 48
# ticker = "btc_krw"
# ticker = ticker.split("_")
# print(ticker)

# 49
# date = "2020-05-01"
# date = date.split("-")
# print(date)

# 50
# data = "039490     "
# data = data.rstrip()
# print(data)

# 51
# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# print(movie_rank)

# 52  !!
# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("배트맨")
# print(movie_rank)

# 53  !!
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)

# 54  !!
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# del movie_rank[3]
# print(movie_rank)

# 55
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)

# 56
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1 + lang2
# print(langs)

# 57  !!
# nums = [1, 2, 3, 4, 5, 6, 7]
# print("max:", max(nums))
# print("min:",min(nums))

# 58
# nums = [1, 2, 3, 4, 5]
# print(sum(nums))

# 59
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# 60
# nums = [1, 2, 3, 4, 5]
# average = sum(nums) / len(nums)
# print(average)

# 61
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])

# 62
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])

# 63
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])

# 64
# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# 65
# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0], interest[2])

# 66  !!
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(" ".join(interest))

# 67
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("/".join(interest))

# 68
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("\n".join(interest))

# 69
# string = "삼성전자/LG전자/Naver"
# string = string.split("/")
# print(string, type(string))

# 70  !!
# data = [2, 4, 3, 1, 5, 10, 9]
# data = sorted(data)
# print(data)
#
# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)

# 71
# my_variable = ()
# print(type(my_variable))

# 72
# movie_rank = "닥터 스트레인지", "스플릿", "럭키"
# print(movie_rank)

# 73
# a = (1, )
# print(a, type(a))

# 74
# t = (1, 2, 3)
# t[0] = 'a'

# 75
# t = 1, 2, 3, 4
# print(type(t))

# 76  !!
# t = ('a', 'b', 'c')
# t = ('A', 'b', 'c')
# print(t)

# 77
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# interest = list(interest)
# print(interest)

# 78
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# interest = tuple(interest)
# print(interest)

# 79  !!
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)

# 80  !!
# a = tuple(range(2, 100, 2))
# print(a)

# 81
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, _, _ = scores
# print(valid_score)

# 82
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, b, *valid_score = scores
# print(valid_score)

# 83
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, *valid_score, b = scores
# print(valid_score)

# 84
# temp = {}

# 85
# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# print(ice)

# 86
# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# ice["죠스바"] = 1200
# ice["월드콘"] = 1500
# print(ice)

# 87
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
#
# print("메로나 가격:", ice["메로나"])

# 88
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
#
# ice["메로나"] = 1300
# print(ice)

# 89
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
#
# del ice["메로나"]
# print(ice)

# 90
# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']

# 91
# inventory = {"메로나": [300, 200],
#              "비비빅": [400, 3],
#              "죠스바": [250, 100]}
# print(inventory)

# 92
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
#
# print(inventory["메로나"][0], "원")

# 93
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
#
# print(inventory["메로나"][1], "개")

# 94
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
#
# inventory["월드콘"] = [500, 7]
# print(inventory)

# 95  !!
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# a = list(icecream.keys())
# print(a)

# 96
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# a = list(icecream.values())
# print(a)

# 97  !!
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# a = sum(icecream.values())
# print(a)

# 98  !!
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
#
# icecream.update(new_product)
# print(icecream)

# 99  !!
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
#
# result = dict(zip(keys, vals))
# print(result)

# 100
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# close_table = dict(zip(date, close_price))
# print(close_table)

# 101
# bool

# 102
# print(3 == 5)

# 103
# print(3 < 5)

# 104
# x = 4
# print(1 < x < 5)

# 105
# print ((3 == 3) and (4 != 3))

# 106
# print(3 => 4)

# 107
# if 4 < 3:
#     print("Hello World")

# 108
# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")

# 109
# if True :
#     print ("1")
#     print ("2")
# else :
#     print("3")
# print("4")

# 110
# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")

# 111  !!
# data = input("입력:")
# print(data * 2)

# 112  !!
# data = input("숫자를 입력하세요:")
# print(int(data) + 10)

# 113
# data = input("입력:")
# if int(data) % 2 == 0 :
#     print("짝수")
#
# else:
#     print("홀수")

# 114  !!
# data = input("입력:")
# num = int(data) + 20
# if num > 255 :
#     print(255)
#
# else:
#     print(num)

# 115
# data = input("입력:")
# num = int(data) - 20
# if num < 0 :
#     print(0)
# elif num > 255:
#     print(255)
# else:
#     print(num)

# 116 !!
# data = input("현재시간:")
# if data[-2:] == "00" :
#     print("정각입니다.")
# else:
#     print("정각이 아닙니다.")

# 117 !!
# fruit = ["사과", "포도", "홍시"]
# data = input("좋아하는 과일은?")
# if data in fruit :
#     print("정답입니다.")
#
# else:
#     print("오답입니다")

# 118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# data = input("입력:")
# if data in warn_investment_list :
#     print("투자경고종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")

# 119  !!
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# data = input("제가좋아하는계절은:")
# if data in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# 120
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# data = input("좋아하는 과일은:")
# if data in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# 121  !!
# data = input("입력:")
# if data.islower():    ## 소문자일경우 True, 대문자면 False.
#     print(data.upper())
# else:
#     print(data.lower())

# 122
# data = input("score:")
# data = int(data)
# if data >= 81 :
#     print("grade is A")
# elif data >= 61 :
#     print("grade is B")
# elif data >= 41:
#     print("grade is C")
# elif data >= 21 :
#     print("grade is D")
# else:
#     print("grade is E")

# 123 !!
# data = input("입력:")
# data = data.split()
# if data[1] == "달러" :
#     print(int(data[0]) * 1167, "원")
# elif data[1] == "엔" :
#     print(int(data[0]) * 1.096, "원")
# elif data[1] == "유로":
#     print(int(data[0]) * 1268, "원")
# else:
#     print(int(data[0]) * 171, "원")

# 환율 = {"달러": 1167,
#       "엔": 1.096,
#       "유로": 1268,
#       "위안": 171}
# data = input("입력:")
# a, b = data.split()
# print(float(a) * 환율[b], "원")

# 124
# data1 = input("input number1:")
# data2 = input("input number2:")
# data3 = input("input number3:")
# data1 = int(data1)
# data2 = int(data2)
# data3 = int(data3)
# if data2 < data1 > data3 :
#     print(data1)
# elif data1 < data2 > data3 :
#     print(data2)
# else:
#     print(data3)

# 125  !!
# data = input("휴대전화 번호 입력:")
# data = data[:3]
# if data == "011":
#     print("당신은 SKT 사용자입니다.")
# elif data == "016":
#     print("당신은 KT 사용자입니다.")
# elif data == "019":
#     print("당신은 LGU 사용자입니다.")
# else:
#     print("알수없음")


# data = input("휴대전화 번호 입력:")
# num = data.split("-")[0]
# if num == "011":
#     com = "SKT"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# else:
#     com = "알수없음"
# print(f"당신은 {com} 사용자 입니다.")

# 126  !!  !!
# data = input("우편번호:")
# if data[2] in ["0", "1", "2"] :
#     print("강북구")
# elif data[2] in ["3", "4", "5"]:
#     print("도봉구")
# else:
#     print("노원구")

# 127
# data = input("주민등록번호:")
# num = data.split("-")[1]
# sex = num[0]
# if sex in ["1", "3"]:
#     print("남자")
# else:
#     print("여자")

# 주민번호 = input("주민등록번호: ")
# 주민번호 = 주민번호.split("-")[1]
# if 주민번호[0] == "1" or 주민번호[0] == "3":
#     print("남자")
# else:
#     print("여자")

# 128  !!
# data = input("주민등록번호: ")
# num = data.split("-")[1]
#
# if 0 <= int(num[1:3]) <= 8 :
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")

# 129  !!
# data = input("주민등록번호: ")
#
# a = (int(data[0]) * 2) + (int(data[1]) * 3) + (int(data[2]) * 4) + (int(data[3]) * 5)\
#     + (int(data[4]) * 6) + (int(data[5]) * 7) + (int(data[7]) * 8) + (int(data[8]) * 9)\
#     + (int(data[9]) * 2) + (int(data[10]) * 3) + (int(data[11]) * 4) + (int(data[12]) * 5)
# b = 11 - (a % 11)
# c = str(b)
#
# if data[-1] == c:
#     print("유효")
# else:
#     print("유효하지않음")

# 130  !!
import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#
# 변동폭 = float(btc['max_price']) - float(btc['min_price'])
# 기준 = float(btc['opening_price']) + 변동폭
# 최고가 = float(btc['max_price'])
#
# if 기준 > 최고가 :
#     print("상승장")
# else:
#     print("하락장")

# 131
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)

# 132
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#   print("#####")

# 133
# for 변수 in ["A", "B", "C"]:
#   print(변수)
#
# print("A")
# print("B")
# print("C")

# 134
# for 변수 in ["A", "B", "C"]:
#   print("출력:", 변수)
#
# print("출력:", "A")
# print("출력:", "B")
# print("출력:", "C")

# 135
# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환:", b)
#
# print("변환:", "a")
# print("변환:", "b")
# print("변환:", "c")

# 136
# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)
#
#
# for 변수 in [10, 20, 30]:
#     print(변수)

# 137
# print(10)
# print(20)
# print(30)
#
# for i in [10, 20, 30]:
#     print(i)

# 138
# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")
#
# for i in [10, 20, 30]:
#     print(i)
#     print("-------")

# 139
# print("++++")
# print(10)
# print(20)
# print(30)
#
# for i in ["++++", 10, 20, 30]:
#     print(i)
#
# print("++++")
# for 변수 in [10, 20, 30]:
#   print(변수)

# 140
# print("-------")
# print("-------")
# print("-------")
# print("-------")
#
# print()
#
# for i in [1, 2, 3, 4]:
#     print("------")

# 141
# 리스트 = [100, 200, 300]
# for i in 리스트:
#     print(i + 10)

# 142
# 리스트 = ["김밥", "라면", "튀김"]
# for i in 리스트:
#     print("오늘의 메뉴:", i)

# 143
# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# for i in 리스트:
#     print(len(i))

# 144
# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i, len(i))

# 145
# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i[0])

# 146
# 리스트 = [1, 2, 3]
# for i in 리스트:
#     print("3 x", i)

# 147  !!
# 리스트 = [1, 2, 3]
# for i in 리스트:
#     print("3 x", i, "=", 3*i)
#
# 리스트 = [1, 2, 3]
# for i in 리스트:
#     print("3 x {} = {}".format(i, 3*i))

# 148
# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[1:]:
#     print(i)

# 149  !!
# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[0],리스트[2]:
#     print(i)
#
# for i in 리스트[::2]:
#     print(i)

# 150
# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[::-1]:
#     print(i)

# 151
# 리스트 = [3, -20, -3, 44]
# for i in 리스트:
#     if i < 0:
#         print(i)

# 152
# 리스트 = [3, 100, 23, 44]
# for i in 리스트:
#     if i % 3 == 0:
#         print(i)

# 153
# 리스트 = [13, 21, 12, 14, 30, 18]
# for i in 리스트:
#     if (i < 20) and (i % 3 == 0):
#         print(i)

# 154
# 리스트 = ["I", "study", "python", "language", "!"]
# for i in 리스트:
#     if len(i) >= 3:
#         print(i)

# 155
# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#     if i.isupper():
#         print(i)

# 156
# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#     if i.islower():
#         print(i)

# 157  !!
# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트:
#     print(i.capitalize())
#
# for i in 리스트:
#     print(i[0].upper() + i[1:])

# 158
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# for i in 리스트:
#     print(i.split(".")[0])
#
# for i in 리스트:
#     split = i.split(".")
#     print(split[0])

# 159   !!
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in 리스트:
#     if i[-1] == "h":
#         print(i)
#
# for i in 리스트:
#     split = i.split(".")
#     if split[1] == "h":
#         print(i)

# 160   !!
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in 리스트:
#     split = i.split(".")
#     if split[1] == "h" or "c":      # 바로 or 로 연결은 안된다.
#         print(i)

# for i in 리스트:
#     split = i.split(".")
#     if split[1] == "h" or split[1] == "c":
#         print(i)

# 161
# for i in range(100):
#     print(i)

# 162
# for i in range(2002, 2051, 4):
#     print(i)

# 163
# for i in range(3, 31, 3):
#     print(i)

# 164
# for i in range(100):
#     print(99 - i)

# 165   !!
# for i in range(10):
#     print(i / 10)

# 166   !!
# for i in range(1, 10):
#     print("3x{} = {}".format(i, 3*i))
#
# for i in range(1, 10) :
#     print (3, "x", i, " = ", 3 * i)

# 167
# for i in range(1, 10, 2):
#     print("3x{} = {}".format(i, 3*i))
#
# num = 3
# for i in range(1, 10) :
#     if i % 2 == 1 :
#         print (num, "x", i, " = ", num * i)

# 168   !!
# a = 0
# for i in range(1, 11):
#     a += i
# print(a)

# 169
# a = 0
# for i in range(1, 11):
#     if i % 2 == 1:
#         a += i
# print(a)
#
# a = 0
# for i in range(1, 11, 2):
#     a += i
# print(a)

# 170
# a = 1
# for i in range(1, 11):
#     a *= i
# print(a)

# 171   !!
# price_list = [32100, 32150, 32000, 32500]
# for i in price_list:
#     print(i)
#
# for i in range(4):
#     print(price_list[i])
#
# for i in range(len(price_list)):    #리스트내용이 변해도 수정할 필요가 없다.
#     print(price_list[i])

# 172   !!
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(i, price_list[i])

# for i, data in enumerate(price_list):
#     print(i, data)

# 173   !!
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(3 - i, price_list[i])

# 174   !!
# price_list = [32100, 32150, 32000, 32500]
# for i in range(1, 4):
#     print(90 + 10 * i, price_list[i])

# 175   !!
# my_list = ["가", "나", "다", "라"]
# for i in range(1, len(my_list)):
#     print(my_list[i-1], my_list[i])

# 176   !!
# my_list = ["가", "나", "다", "라", "마"]
#
# for i in range( len(my_list) - 2 ):
#     print(my_list[i], my_list[i+1], my_list[i+2])

# 177   !!
# my_list = ["가", "나", "다", "라"]
# for i in range(3, 0, -1):
#     print(my_list[i], my_list[i-1])

# 178
# my_list = [100, 200, 400, 800]
# for i in range(len(my_list) - 1):
#     print(my_list[i+1] - my_list[i])

# 179
# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(len(my_list) -2):
#         print((my_list[i] + my_list[i+1] + my_list[i+2]) / 3)

# 180
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# volatility = []
# for i in range(len(low_prices)):
#     a = high_prices[i] - low_prices[i]
#     volatility.append(a)
# print(volatility)

# 181
# apart = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]
# print(apart, type(apart))

# 182
# stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]
# print(stock)

# 183
# stock = {"시가" : [100, 200, 300], "종가" : [80, 210, 330]}
# print(stock.values())

# 184
# stock = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200]}
# print(stock)

# 185   !!
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(len(apart)):
#     print(apart[i][0], "호")
#     print(apart[i][1], "호")

# for 층 in apart:
#     for 집 in 층:
#         print(집, "호")

# 186
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart[::-1]:
#     for house in row:
#         print(house, "호")

# 187
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart[::-1]:
#     for col in row[::-1]:
#         print(col, "호")

# 188
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#     for col in row:
#         print(col, "호")
#         print("-" * 5)

# 189
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#     for col in row:
#         print(col, "호")
#     print("-" * 5)

# 190
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#     for col in row:
#         print(col, "호")
# print("-" * 5)

# 191
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
#
# for row in data:
#     for col in row :
#         print(col * 1.00014)

# 192
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
#
# for row in data:
#     for col in row:
#         print(col * 1.00014)
#     print("-"*5)

# 193
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for row in data:
#     for col in row:
#         a = col * 1.00014
#         result.append(a)
# print(result)

# 194   !!
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for line in data:
#     sub =[]
#     for col in line:
#         sub.append(col * 1.00014)
#     result.append(sub)
# print(result)


# 195
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for row in ohlc[1:]:
#     print(row[3])

# 196
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for row in ohlc[1:]:
#     if row[3] > 150:
#         print(row[3])

# 197
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for row in ohlc[1:]:
#     if row[3] >= row[0]:
#         print(row[3])

# 198
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# volatility = []
# for row in ohlc[1:]:
#     diff = row[1] - row[2]
#     volatility.append(diff)
# print(volatility)

# 199
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# for row in ohlc[1:]:
#     if row[3] > row[0]:
#         print(row[1] - row[2])

# 200
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# total = 0
# for row in ohlc[1:]:
#     rate = row[0] - row[3]
#     total += rate
# print(total)

# 201
# def print_coin():
#     print("비트코인")
# print_coin()

# 202
# print_coin()

# 203
# def print_coin():
#     print("비트코인")
#
# for i in range(100):
#     print_coin()

# 204
# def print_coin():
#     for i in range(100):
#         print("비트코인")
# print_coin()

# # 205
# hello()
# def hello():
#     print("Hi")

# 206
# def message() :
#     print("A")
#     print("B")
#
# message()
# print("C")
# message()

# 207
# print("A")
#
# def message() :
#     print("B")
#
# print("C")
# message()

# 208
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()

# 209
# def message1():
#     print("A")
#
# def message2():
#     print("B")
#     message1()
#
# message2()

# 210
# def message1():
#     print("A")
#
# def message2():
#     print("B")
#
# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()
#
# message3()

# 211
# def 함수(문자열) :
#     print(문자열)
#
# 함수("안녕")
# 함수("Hi")

# 212
# def 함수(a, b) :
#     print(a + b)
#
# 함수(3, 4)
# 함수(7, 8)

# 213
# def 함수(문자열) :
#     print(문자열)

# 214
# def 함수(a, b) :
#     print(a + b)
#
# 함수("안녕", 3)

# 215
# def print_with_smile():
#     data = input("입력:")
#     print(data + ":D")
#
# print_with_smile()

# def print_with_smile(str):
#     print(str + ":D")
#
# print_with_smile("asdf")

# 216
# def print_with_smile(str):
#     print(str + ":D")
#
# print_with_smile("안녕하세요")

# 217
# def print_upper_price(current):
#     print(current * 1.3)
#
# print_upper_price(10000)

# 218
# def print_sum(a, b):
#     print(a + b)
#
# print_sum(100, 500)

# 219
# def print_arithmetic_operation(a, b):
#     print(f"{a} + {b} = {a + b}")
#     print(f"{a} - {b} = {a - b}")
#     print(f"{a} * {b} = {a * b}")
#     print(f"{a} / {b} = {a / b}")
# print_arithmetic_operation(3, 4)

# 220
# def  print_max(a, b, c):
#     if b < a > c:
#         print(a)
#     elif a < b > c:
#         print(b)
#     else:
#         print(c)
#
# print_max(1, 2, 3)

# 221
# def print_reverse(string):
#     print(string[::-1])
#
# print_reverse("python")

# 222
# def score(data):
#     avr = sum(data) / len(data)
#     print(avr)
#
# score([1, 2, 3])

# 223
# def even(data):
#     for i in data:
#         if i % 2 == 0:
#             print(i)
#
# even ([1, 3, 2, 10, 12, 11, 15])

# 224
# def print_keys(data):
#     for i in data.keys():
#         print(i)
#
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225   !!
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
#
# def print_value_by_key(a, b):
#     print(a[b])
#
# print_value_by_key(my_dict, "10/26")

# 226       !!
# def print_5xn(string):
#     num = len(string) / 5
#     for i in range(int(num) + 1):
#         print(string[i*5 : i*5+5])
#
# print_5xn("아이엠어보이유알어걸")

# 227
# def print_mxn(string, b):
#     num = len(string) / b
#     for i in range(int(num) +1):
#         print(string[i * b : i * b + b])
#
# print_mxn("아이엠어보이유알어걸", 3)

# 228
# def calc_monthly_salary(salary):
#     month_salary = int(salary / 12)   # 형변환
#     return month_salary
#
# pay = calc_monthly_salary(12000000)
# print(pay)

# 229
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(a=100, b=200)

# 230
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(b=100, a=200)

# 231
# def n_plus_1 (n) :
#     result = n + 1
#
# n_plus_1(3)
# print (result)

# 232
# def make_url(make):
#     url = "www." + make + ".com"
#     return url
#
# result = make_url("naver")
# print(result)

# 233
# def make_list(string):
#     list = []
#     for i in string:
#         list.append(i)
#     return list
#
# mylist = make_list("abcd")
# print(mylist)


# def make_list(string):
#     return list(string)
#
# mylist = make_list("abcd")
# print(mylist)

# 234
# def  pickup_even(data):
#     list = []
#     for i in data:
#         if i % 2 == 0:
#             list.append(i)
#     return list
#
# even = pickup_even([3, 4, 5, 6, 7, 8])
# print(even)

# 235
# def convert_int(data):
#     data = int(data.replace(",", ""))
#     return data
#
# int = convert_int("1,234,567")
# print(int, type(int))

# 236   !!
# def 함수(num) :
#     return num + 4
#
# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)

# 237
# def 함수(num) :
#     return num + 4
#
# c = 함수(함수(함수(10)))
# print(c)

# 238
# def 함수1(num) :
#     return num + 4
#
# def 함수2(num) :
#     return num * 10
#
# a = 함수1(10)
# c = 함수2(a)
# print(c)

# 239
# def 함수1(num) :
#     return num + 4
#
# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)
#
# c = 함수2(10)
# print(c)

# 240
# def 함수0(num) :
#     return num * 2
#
# def 함수1(num) :
#     return 함수0(num + 2)
#
# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)
#
# c = 함수2(2)
# print(c)

# 241
# import datetime
#
# now = datetime.datetime.now()
# print(now)

# 242
# import datetime
#
# now = datetime.datetime.now()
# print(now, type(now))

# 243
# import datetime
#
# now = datetime.datetime.now()
# for i in range(5):
#     days = now + datetime.timedelta(-5 + i)
#     print(days)

# for i in range(-5, 0)   # -5, -4, -3...   !!
#     delta = datetime.timedelta(days=i)
#     print(now + delta)
#

# 244   !!  시간,분, 초 만 출력
# import datetime
#
# now = datetime.datetime.now()
# a = now.strftime("%H:%M:%S")
# print(a)

# 245   !!  문자열을 datetime 타입으로 변환
# import datetime
#
# day = "2020-05-04"
# ret = datetime.datetime.strptime(day, "%Y-%m-%d")
# print(ret, type(ret))

# 246   !!
# import datetime
# import time
#
# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

# 247   !!
# import os               # os.rename()
# from os import rename   # rename()
# from os import *        # getcwd(), rename()...
# import os as myos       # myos.getcwd()

# 248   !!  현재 디렉터리의 경로
# import os
# ret = os.getcwd()
# print(ret, type(ret))

# 249   !!  파일이름 변경
# import os
#
# os.rename("C:/Users/user/Desktop/aa.txt", "C:/Users/user/Desktop/bb.txt")

# 250   !!  numpy모듈의 arange를 사용하면 소수점 증가값을 사용할수있다 .  range는 정수만 가능.
# import numpy
#
# for i in numpy.arange(0, 5, 0.1):
#     print(i)

# 251
'''
클래스 = 붕어빵틀
객체, 인스턴스, 오브젝트 = 붕어빵
'''

# 252
# class Human:
#     pass

# 253
# class Human:
#     pass
#
# areum = Human()

# 254
# class Human:
#     def __init__(self):
#         print("응애응애")
#
# areum = Human()

# 255
# class Human:
#     def __init__(self, 이름, 나이, 성별):
#         self.이름, self.나이, self.성별 = 이름, 나이 , 성별
#
# areum = Human("아름", 25, "여자")
# print(areum.이름)

# 256
# class Human:
#     def __init__(self, 이름, 나이, 성별):
#         self.이름, self.나이, self.성별 = 이름, 나이 , 성별
#
# areum = Human("아름", 25, "여자")
# print(f"이름: {areum.이름}, 나이: {areum.나이}, 성별: {areum.성별}")

# 257
# class Human:
#     def __init__(self, 이름, 나이, 성별):
#         self.이름, self.나이, self.성별 = 이름, 나이 , 성별
#
#     def who(self):
#         print(f"이름: {self.이름}, 나이: {self.나이}, 성별: {self.성별}")
#         print("이름: {}, 나이: {}, 성별: {}".format(self.이름, self.나이, self.성별))
#
# areum = Human("아름", 25, "여자")
# areum.who()

# 258
# class Human:
#     def __init__(self, 이름, 나이, 성별):
#         self.이름, self.나이, self.성별 = 이름, 나이 , 성별
#
#     def who(self):
#         print(f"이름: {self.이름}, 나이: {self.나이}, 성별: {self.성별}")
#         print("이름: {}, 나이: {}, 성별: {}".format(self.이름, self.나이, self.성별))
#
#     def setinfo(self, 이름, 나이, 성별):
#         self.이름, self.나이, self.성별 = 이름, 나이, 성별
#
# areum = Human("모름", "미상", "모름")
# areum.who()
#
# areum.setinfo("아름", 25, "여자")
# areum.who()

# 259
# class Human:
#     def __init__(self, 이름, 나이, 성별):     # 객체가 생성될때 자동으로 호출되는 메소드(생성자)
#         self.이름, self.나이, self.성별 = 이름, 나이 , 성별
#
#     def __del__(self):      ## 객체가 메모리에서 소멸될때 자동으로 호출되는 메소드(소멸자)
#         print("나의 죽음을 알리지 마라")
#
#     def who(self):
#         print(f"이름: {self.이름}, 나이: {self.나이}, 성별: {self.성별}")
#         print("이름: {}, 나이: {}, 성별: {}".format(self.이름, self.나이, self.성별))
#
#     def setinfo(self, 이름, 나이, 성별):
#         self.이름, self.나이, self.성별 = 이름, 나이, 성별
#
# areum = Human("아름", 25, "여자")
# del(areum)

# 260

# 261
# class Stock:
#     pass

# 262
# class Stock:
#     def __init__(self, 종목명, 종목코드):
#         self.종목명 = 종목명
#         self.종목코드 = 종목코드
#
# 삼성 = Stock("삼성", "005930")
# print(삼성.종목코드, 삼성.종목명)

# 263
# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code
#
#     def set_name(self, name):
#         self.name = name
#
# a = Stock("LG전자", "005930")
# print(a.code, a.name)
# a.set_name("삼성전자")
# print(a.name, a.code)

# 264
# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_code(self, code):
#         self.code = code
#
# a = Stock(None, None)
# a.set_code("005930")
# print(a.code)

# 265
# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_code(self, code):
#         self.code = code
#
#     def get_name(self):
#         return self.name
#
#     def get_code(self):
#         return self.code
#
# 삼성 = Stock("삼성전자", "005930")
# print(삼성.name)
# print(삼성.code)
# print(삼성.get_name())
# print(삼성.get_code())

# 266
# class Stock:
#     def __init__(self, name, code, per, pbr, rate):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.rate = rate
#
#         self.per = float(self.per)
#         self.pbr = float(self.pbr)
#         self.rate = float(self.rate)
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_code(self, code):
#         self.code = code
#
#     def get_name(self):
#         return self.name
#
#     def get_code(self):
#         return self.code

# 267
# class Stock:
#     def __init__(self, name, code, per, pbr, rate):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.rate = rate
#
#         # self.per = float(self.per)
#         # self.pbr = float(self.pbr)
#         # self.rate = float(self.rate)
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_code(self, code):
#         self.code = code
#
#     def get_name(self):
#         return self.name
#
#     def get_code(self):
#         return self.code
#
#     def print(self):
#         print(self.name, self.code, self.per, self.pbr, self.rate)
#
# 삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# 삼성.print()

# 268
# class Stock:
#     def __init__(self, name, code, per, pbr, rate):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.rate = rate
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_code(self, code):
#         self.code = code
#
#     def set_per(self, per):
#         self.per = per
#
#     def set_pbr(self, pbr):
#         self.pbr = pbr
#
#     def set_rate(self, rate):
#         self.rate = rate
#
#     def get_name(self):
#         return self.name
#
#     def get_code(self):
#         return self.code
#
#     def print(self):
#         print(self.name, self.code, self.per, self.pbr, self.rate)

# 269
# class Stock:
#     def __init__(self, name, code, per, pbr, rate):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.rate = rate
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_code(self, code):
#         self.code = code
#
#     def set_per(self, per):
#         self.per = per
#
#     def set_pbr(self, pbr):
#         self.pbr = pbr
#
#     def set_rate(self, rate):
#         self.rate = rate
#
#     def get_name(self):
#         return self.name
#
#     def get_code(self):
#         return self.code
#
#     def print(self):
#         print(self.name, self.code, self.per, self.pbr, self.rate)
#
# 삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# 삼성.print()
# 삼성.set_per(12.75)
# 삼성.print()
# print(삼성.per)

# 270  !!
# class Stock:
#     def __init__(self, name, code, per, pbr, rate):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.rate = rate
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_code(self, code):
#         self.code = code
#
#     def set_per(self, per):
#         self.per = per
#
#     def set_pbr(self, pbr):
#         self.pbr = pbr
#
#     def set_rate(self, rate):
#         self.rate = rate
#
#     def get_name(self):
#         return self.name
#
#     def get_code(self):
#         return self.code
#
#     def print(self):
#         print(self.name, self.code, self.per, self.pbr, self.rate)
#
# list = []
#
# 삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# 현대 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
# 엘지 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
#
# list.append(삼성)
# list.append(현대)
# list.append(엘지)
#
# for i in list:
#     print(i.code, i.per)

# 271
import random

# num = random.randint(0, 99)
# num = str(num)
# print(num.zfill(5), type(num))  ## zfill(숫자) 함수는, 원하는자리숫자대로 앞에 0 을 붙여서 만들어준다.

# class Account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 3-2-6
#         num1 = random.randint(0, 999)       # 1 -> "1" -> "001"
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
# kim = Account("김민수", 1000)
# print(kim.name)
# print(kim.balance)
# print(kim.account_number)
# print(kim.bank)

# 272
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 계좌번호 생성 3-2-6
#         num1 = random.randint(0, 999)       # 1 -> "1" -> "001"
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
# kim = Account("김민수", 1000)
# lee = Account("이희정", 1000)
# print(Account.account_count)

# 273
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 계좌번호 생성 3-2-6
#         num1 = random.randint(0, 999)       # 1 -> "1" -> "001"
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
#     @ classmethod
#     def get_account_num(cls):
#         print(cls.account_count)
#
# kim = Account("김민수", 1000)
# lee = Account("이희정", 1000)
#
# kim.get_account_num()

# 274
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 계좌번호 생성 3-2-6
#         num1 = random.randint(0, 999)       # 1 -> "1" -> "001"
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
#     @ classmethod
#     def get_account_num(cls):
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount >= 1 :
#             self.balance += amount
#             print("{} 이 입금되었습니다".format(amount))
#
#         else:
#             print("입금액은 최소 1원 이상이어야 합니다.")
#
# kim = Account("김민수", 1000)
# lee = Account("이희정", 1000)
#
# kim.deposit(100)
# print(kim.balance)

# 275
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 계좌번호 생성 3-2-6
#         num1 = random.randint(0, 999)       # 1 -> "1" -> "001"
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
#     @ classmethod
#     def get_account_num(cls):
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount >= 1 :
#             self.balance += amount
#             print("{} 이 입금되었습니다".format(amount))
#
#         else:
#             print("입금액은 최소 1원 이상이어야 합니다.")
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#             print("{} 이 출금되었습니다".format(amount))
#         else:
#             print("출금은 계좌의 잔고 이상으로 할 수 없습니다.")
#
# kim = Account("김민수", 1000)
# lee = Account("이희정", 1000)
#
# kim.withdraw(1000)
# print(kim.balance)

# 276
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 계좌번호 생성 3-2-6
#         num1 = random.randint(0, 999)       # 1 -> "1" -> "001"
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
#     @ classmethod
#     def get_account_num(cls):
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount >= 1 :
#             self.balance += amount
#             print("{} 이 입금되었습니다".format(amount))
#
#         else:
#             print("입금액은 최소 1원 이상이어야 합니다.")
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#             print("{} 이 출금되었습니다".format(amount))
#         else:
#             print("출금은 계좌의 잔고 이상으로 할 수 없습니다.")
#
#     def disply_info(self):
#         print("은행이름: {}".format(self.bank))
#         print(f"예금주: {self.name}")
#         print(f"계좌번호: {self.account_number}")
#         print("잔고: {:,}".format(self.balance))      ## 천단위 숫자 쉼표 구분하는 방법. format활용
#
# kim = Account("김민수", 10000000)
# lee = Account("이희정", 1000)
#
# kim.disply_info()

# 277
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 계좌번호 생성 3-2-6
#         num1 = random.randint(0, 999)       # 1 -> "1" -> "001"
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
#     @ classmethod
#     def get_account_num(cls):
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount >= 1 :
#             self.balance += amount
#             print("{} 이 입금되었습니다".format(amount))
#             self.deposit_count += 1
#
#             if self.deposit_count % 5 == 0:     ## 5, 10, 15 ...
#                 # 이자 지급
#                 self.balance = self.balance * 1.01
#         else:
#             print("입금액은 최소 1원 이상이어야 합니다.")
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#             print("{} 이 출금되었습니다".format(amount))
#         else:
#             print("출금은 계좌의 잔고 이상으로 할 수 없습니다.")
#
#     def disply_info(self):
#         print("은행이름: {}".format(self.bank))
#         print(f"예금주: {self.name}")
#         print(f"계좌번호: {self.account_number}")
#         print("잔고: {:,}".format(self.balance))      ## 천단위 숫자 쉼표 구분하는 방법. format활용
#
# kim = Account("김민수", 10000)
# lee = Account("이희정", 1000)
#
# kim.deposit(10000)
# kim.deposit(10000)
# kim.deposit(10000)
# kim.deposit(10000)
# kim.deposit(10000)
# print(kim.balance)

# 278
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 계좌번호 생성 3-2-6
#         num1 = random.randint(0, 999)       # 1 -> "1" -> "001"
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
#     @ classmethod
#     def get_account_num(cls):
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount >= 1 :
#             self.balance += amount
#             print("{} 이 입금되었습니다".format(amount))
#             self.deposit_count += 1
#
#             if self.deposit_count % 5 == 0:     ## 5, 10, 15 ...
#                 # 이자 지급
#                 self.balance = self.balance * 1.01
#         else:
#             print("입금액은 최소 1원 이상이어야 합니다.")
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#             print("{} 이 출금되었습니다".format(amount))
#         else:
#             print("출금은 계좌의 잔고 이상으로 할 수 없습니다.")
#
#     def disply_info(self):
#         print("은행이름: {}".format(self.bank))
#         print(f"예금주: {self.name}")
#         print(f"계좌번호: {self.account_number}")
#         print("잔고: {:,}".format(self.balance))      ## 천단위 숫자 쉼표 구분하는 방법. format활용
#
# total_account = []
#
# kim = Account("김민수", 10000000)
# lee = Account("이희정", 1000)
# park = Account("박수정", 10000)

# total_account.append(kim)
# total_account.append(lee)
# total_account.append(park)
#
# print(total_account)

# 279
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 계좌번호 생성 3-2-6
#         num1 = random.randint(0, 999)       # 1 -> "1" -> "001"
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
#     @ classmethod
#     def get_account_num(cls):
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount >= 1 :
#             self.balance += amount
#             print("{} 이 입금되었습니다".format(amount))
#             self.deposit_count += 1
#
#             if self.deposit_count % 5 == 0:     ## 5, 10, 15 ...
#                 # 이자 지급
#                 self.balance = self.balance * 1.01
#         else:
#             print("입금액은 최소 1원 이상이어야 합니다.")
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#             print("{} 이 출금되었습니다".format(amount))
#         else:
#             print("출금은 계좌의 잔고 이상으로 할 수 없습니다.")
#
#     def disply_info(self):
#         print("은행이름: {}".format(self.bank))
#         print(f"예금주: {self.name}")
#         print(f"계좌번호: {self.account_number}")
#         print("잔고: {:,}".format(self.balance))      ## 천단위 숫자 쉼표 구분하는 방법. format활용
#
# total_account = []
#
# kim = Account("김민수", 100000000)
# lee = Account("이희정", 100000000)
# park = Account("박수정", 10000)
#
# total_account.append(kim)
# total_account.append(lee)
# total_account.append(park)
#
# for i in total_account:
#     if i.balance >= 1000000:
#         i.disply_info()
#         print()

# 280
# class Account:
#     # class variable
#     account_count = 0
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#         self.deposit_log = []
#         self.withdraw_log = []
#
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         # 계좌번호 생성 3-2-6
#         num1 = random.randint(0, 999)       # 1 -> "1" -> "001"
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#
#         self.account_number = num1 + '-' + num2 + '-' + num3
#
#         Account.account_count += 1
#
#     @ classmethod
#     def get_account_num(cls):
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount >= 1 :
#             self.deposit_log.append(amount)
#             self.balance += amount
#             print("{} 이 입금되었습니다".format(amount))
#             self.deposit_count += 1
#
#             if self.deposit_count % 5 == 0:     ## 5, 10, 15 ...
#                 # 이자 지급
#                 self.balance = self.balance * 1.01
#         else:
#             print("입금액은 최소 1원 이상이어야 합니다.")
#
#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.withdraw_log.append(amount)
#             self.balance -= amount
#             print("{} 이 출금되었습니다".format(amount))
#         else:
#             print("출금은 계좌의 잔고 이상으로 할 수 없습니다.")
#
#     def disply_info(self):
#         print("은행이름: {}".format(self.bank))
#         print(f"예금주: {self.name}")
#         print(f"계좌번호: {self.account_number}")
#         print("잔고: {:,}".format(self.balance))      ## 천단위 숫자 쉼표 구분하는 방법. format활용
#
#     def withdraw_history(self):
#         self.count = 1
#         for i in self.withdraw_log:
#             print(str(self.count) + "회:", i)
#             self.count += 1
#
#     def deposit_history(self):
#         self.count = 1
#         for i in self.deposit_log:
#             print(str(self.count) + "회:", i)
#             self.count += 1
#
# k = Account("김씨", 1000)
# k.deposit(100)
# k.deposit(200)
# k.deposit(300)
# k.deposit_history()

# 281
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
# car = 차(2, 1000)
# print(car.바퀴)
# print(car.가격)

# 282
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
# class 자전차(차):
#   pass

# 283
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
# class 자전차(차):
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
# bicycle = 자전차(2, 100)
# print(bicycle.가격)

# 284
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         super().__init__(바퀴, 가격)        ## override : 부모클래스의 인자값이 동일하므로, 부모클래스의 바퀴, 가격을 호출해서 가져다 쓴다.
#         self.구동계 = 구동계
#
# bicycle = 자전차(2, 100, "시마노")
# print(bicycle.구동계)
# print(bicycle.바퀴)

# 285
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         super().__init__(바퀴, 가격)
#         self.구동계 = 구동계
#
# class 자동차(차):
#     def __init__(self, 바퀴, 가격):
#         super().__init__(바퀴, 가격)
#
#     def 정보(self):
#         print("바퀴수", self.바퀴)
#         print("가격", self.가격)

# car = 자동차(4, 1000)
# car.정보()

# 286
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
#     def 정보(self):
#         print("바퀴수", self.바퀴)
#         print("가격", self.가격)
#
# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         super().__init__(바퀴, 가격)
#         self.구동계 = 구동계
#
# class 자동차(차):
#     def __init__(self, 바퀴, 가격):
#         super().__init__(바퀴, 가격)
#
# bicycle = 자전차(2, 100, "시마노")
# bicycle.정보()

# 287
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
#     def 정보(self):
#         print("바퀴수", self.바퀴)
#         print("가격", self.가격)
#
# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         super().__init__(바퀴, 가격)
#         self.구동계 = 구동계
#
#     def 정보(self):
#         super().정보()
#         print("구동계", self.구동계)
#
#
# class 자동차(차):
#     def __init__(self, 바퀴, 가격):
#         super().__init__(바퀴, 가격)
#
# bicycle = 자전차(2, 100, "시마노")
# bicycle.정보()

# 288
# class 부모:
#   def 호출(self):
#     print("부모호출")
#
# class 자식(부모):
#   def 호출(self):
#     print("자식호출")
#
# 나 = 자식()
# 나.호출()

# 289
# class 부모:
#   def __init__(self):
#     print("부모생성")
#
# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
#
# 나 = 자식()