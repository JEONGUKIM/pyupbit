### 파이썬 분기문(101~ 130), 반복문(131~200) ####
# 101
# bool 타입

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

# 111
# data = input(">> ")
# print(data * 2)

# 112
# data = input("숫자를 입력하세요: ")
# print(int(data) + 10)

# 113
# data = input("입력: ")
# if int(data) % 2 == 0:
#     print("짝수")
#
# else:
#     print("홀수")

# 114
# data = input(">> ")
# data1 = int(data) + 20
# if data1 > 255:
#     print(255)
# else:
#     print(data1)

# 115
# data = input(">> ")
# data1 = int(data) - 20
# if data1 < 0:
#     print(0)
# elif data1 > 255:
#     print(255)
# else:
#     print(data1)

# 116   !!
# data = input("현재시간: ")
#
# if data[-2:] == "00":
#     print("정각입니다")
#
# else:
#     print("정각이 아닙니다.")

# 117
# fruit = ["사과", "포도", "홍시"]
# data = input("입력: ")
# if data in fruit:
#     print("정답")
#
# else:
#     pass

# 118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
#
# data = input("입력: ")
# if data in warn_investment_list:
#     print("투자 경고 종목입니다.")
#
# else:
#     print("투자 경고 종목이 아닙니다.")


# 119    !!
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# data = input("입력: ")
# if data in fruit:          ## 기본적으로 keys 함수를 안써도   키값을 가져옴.
#     print("정답입니다.")
#
# else:
#     print("NO")
#
# # 120
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# data = input("입력: ")
# if data in fruit.values():
#     print("정답")
#
# else:
#     print("NO")

# 121
# data = input(">> ")
# if data.islower():        ## 소문자여부 판별, 소문자면 True, 대문자면 False
#     print(data.upper())
# else:
#     print(data.lower())

# 122
# data = input("score: ")
# data = int(data)
# if 80 < data <=100:
#     print("A")
#
# elif data > 60:
#     print("B")
# elif data > 40:
#     print("C")
# elif data > 20:
#     print("D")
# else:
#     print("E")

# 123
# 달러 = 1167; 엔 = 1.096; 유로 = 1268; 위안 = 171
# data = input("입력: ")
# data = data.split()
# data1 = data[1]
# data2 = int(data[0])
#
# if data1 == "달러":
#     print(data2 * 달러)
# elif data1 == "엔":
#     print(data2 * 엔)
#
# elif data1 == "유로":
#     print(data2 * 유로)
#
# else:
#     print(data2 * 위안)

# 124
# data1 = input("입력: ")
# data2 = input("입력: ")
# data3 = input("입력: ")
# data1 = int(data1) ; data2 = int(data2) ; data3 = int(data3)
#
# if  data2 < data1 > data3:
#     print(data1)
# elif data1 < data2 > data3:
#     print(data2)
# else:
#     print(data3)

# 125
# data = input("번호: ")
# if data[:3] == "011":
#     mobile = "SKT"
# elif data[:3] == "016":
#     mobile = "KT"
# elif data[:3] == "019":
#     mobile = "LGU+"
# else:
#     mobile = "알수없음"
# print(f"당신은{mobile} 사용자입니다.")

# 126   !!
# data = input("우편번호: ")
# if data[:3] in ["010", "011", "012"]:
#     print("강북구")
# elif data[:3] in ["013", "014", "015"]:
#     print("도봉구")
# else:
#     print("노원구")

# 127
# data = input("주번: ")
# data = data.split("-")[1]
# if data[0] in ["1", "3"]:       # if data[0] == "1" or data[0] == "3":
#     print("남자")
# else:
#     print("여자")

# 128   !!
# data = input("주번: ")
# data = data.split("-")[1]
#
# if 0 <= int(data[1:3]) <=8:
#     print("서울")
# else:
#     print("서울이 아닙니다.")

# 129   !!
# data = input("주번 유효성 확인: ")
# data = data.split("-")
# data0 = data[0]
# data1 = data[1]
#
# a = int(data0[0])*2 + int(data0[1])*3 + int(data0[2])*4 + int(data0[3])*5 + int(data0[4])*6 + int(data0[5])*7 \
#     + int(data1[0])*8 + int(data1[1])*9 + int(data1[2])*2 + int(data1[3])*3 + int(data1[4])*4 + int(data1[5])*5
#
# chcek_num = 11 - (a % 11)
# chcek_num = str(chcek_num)
#
# if data1[-1] == chcek_num[-1]:
#     print("유효")
#
# else:
#     print("불일치")

# 130   !!
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#
# 최고가 = float(btc["max_price"])
# 최소가 = float(btc['min_price'])
# 시가 = float(btc['opening_price'])
# 변동폭 = 최고가 - 최소가
#
# if 시가 + 변동폭 > 최고가:
#     print("상승장")
# else:
#     print("하락장")
#
# print(btc)

##### 파이썬 반복문 #######

# 131
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)
#
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
# for i in [10, 20, 30]:
#     print(i)

# 137
# for i in [10, 20, 30]:
#     print(i)

# 138
# for i in [10, 20, 30]:
#     print(i); print("-" * 7)

# 139
# print("+++++")
# for i in [10, 20, 30]:
#     print(i)

# 140
# for i in range(4):
#     print("-------")
#
# for i in [1, 2, 3, 4]:
#     print("-------")

# 141
# 리스트 = [100, 200, 300]
#
# for i in 리스트:
#     print(i + 10)

# 142
# 리스트 = ["김밥", "라면", "튀김"]
#
# for i in 리스트:
#     print("오늘의 메뉴:", i)

# 143
# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
#
# for i in 리스트:
#     print(len(i))

# 144
# 리스트 = ['dog', 'cat', 'parrot']
#
# for i in 리스트:
#     print(i, len(i))

# 145
# 리스트 = ['dog', 'cat', 'parrot']
#
# for i in 리스트:
#     print(i[0])

# 146
# 리스트 = [1, 2, 3]
#
# for i in 리스트:
#     print("3 X", i)

# 147
# 리스트 = [1, 2, 3]
#
# for i in 리스트:
#     print(f"3 x {i} = {3 *i}")

# 148
# 리스트 = ["가", "나", "다", "라"]
#
# for i in 리스트[1:]:
#     print(i)

# 149
# 리스트 = ["가", "나", "다", "라"]
#
# for i in 리스트[::2]:
#     print(i)

# 150
# 리스트 = ["가", "나", "다", "라"]
#
# for i in 리스트[::-1]:
#     print(i)

# 151
# 리스트 = [3, -20, -3, 44]
#
# for i in 리스트:
#     if i < 0 :
#         print(i)

# 152
# 리스트 = [3, 100, 23, 44]
#
# for i in 리스트:
#     if i % 3 == 0:
#         print(i)

# 153
# 리스트 = [13, 21, 12, 14, 30, 18]
#
# for i in 리스트:
#     if i < 20 and i % 3 == 0:
#         print(i)

# 154
# 리스트 = ["I", "study", "python", "language", "!"]
#
# for i in 리스트:
#     if len(i) > 2:
#         print(i)

# 155
# 리스트 = ["A", "b", "c", "D"]
#
# for i in 리스트:
#     if i.isupper():
#         print(i)

# 156
# 리스트 = ["A", "b", "c", "D"]
#
# for i in 리스트:
#     if i.islower():
#         print(i)

# 157
# 리스트 = ['dog', 'cat', 'parrot']
#
# for i in 리스트:
#     print(i.capitalize())
#
# for i in 리스트:
#     print(i[0].upper() + i[1:])

# 158
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
#
# for i in 리스트:
#     a = i.split(".")
#     print(a[0])

# 159
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
#
# for i in 리스트:
#     if i[-1] in "h" :
#         print(i)

# 160
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
#
# for i in 리스트:
#     a = i.split(".")[1]
#     if a == "h" or a == "c":
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

# 165
# for i in range(0, 10):
#     print(i / 10)

# 166
# for i in range(1, 10):
#     print(f"3x{i} = {3 * i}")

# 167
# for i in range(1, 10, 2):
#     print(f"3x {i} = {3 * i}")

# 168
# a = 0
# for i in range(1, 11):
#     a += i
# print(a)

# 169
# b = 0
# for i in range(1, 11, 2):
#     b += i
# print(b)

# 170
# c = 1
# for i in range(1, 11):
#     c *= i
# print(c)

# 171
# price_list = [32100, 32150, 32000, 32500]
# for i in range(4):
#     print(price_list[i])

# 172
# price_list = [32100, 32150, 32000, 32500]
# for i in range(4):
#     print(i, price_list[i])

# 173
# price_list = [32100, 32150, 32000, 32500]
# for i in range(4):
#     print(3 - i, price_list[i])
#
# print()
#  !!
# for i in range(len(price_list)):
#     print((len(price_list) - 1) -i, price_list[i])

# 174   !!
# price_list = [32100, 32150, 32000, 32500]
# for i in range(1, 4):
#     print(i * 10 + 90, price_list[i])

# 175   !!
# my_list = ["가", "나", "다", "라"]
# for i in range(1, len(my_list)):
#     print(my_list[i-1], my_list[i])

# 176
# my_list = ["가", "나", "다", "라", "마"]
# for i in range(2, len(my_list)):
#     print(my_list[i-2], my_list[i-1], my_list[i])

# 177       !!
# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list) -1, 0, -1):
#     print(my_list[i], my_list[i-1])

# 178
# my_list = [100, 200, 400, 800]
# for i in range(len(my_list) - 1):
#     print(my_list[i+1] - my_list[i])

# 179
# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(len(my_list)-2):
#     print((my_list[i] + my_list[i+1] + my_list[i+2]) / 3)

# 180
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
#
# volatility = []
# for i in range(len(high_prices)):
#     band = high_prices[i] - low_prices[i]
#     volatility.append(band)
# print(volatility)

# 181
# apart = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]
# print(apart)

# 182   !!
# stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]
# print(stock)

# 183
# stock = {"시가":[100, 200, 300], "종가":[80, 210, 330]}
# print((stock))

# 184
# stock = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200]}
# print(stock)

# 185   !!
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#     for i in row:
#         print(i, "호")

# 186
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart[::-1]:
#     for i in row:
#         print(i)
#
# 187
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart[::-1]:
#     for i in row[::-1]:
#         print(i)

# 188
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#     for i in row:
#         print(i)
#         print("----")

# 189
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#     for i in row:
#         print(i)
#     print("-----")

# 190
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#     for i in row:
#         print(i, "호")
# print("-----")

# 191
# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for row in data:
#     for i in row:
#         print(i * 1.00014)

# 192
# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for row in data:
#     for i in row:
#         print(i * 1.00014)
#     print("-----")

# 193
# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
#
# result = []
# for row in data:
#     for i in row:
#         result.append(i * 1.00014)
# print(result)

# 194   !!
# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
#
# result = [ ]
# for row in data:
#     sub = [ ]
#     for i in row:
#         sub.append(i * 1.00014)
#     result.append(sub)
# print(result)

# 195
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# for row in ohlc[1:]:
#     print(row[3])

# 196
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# for row in ohlc[1:]:
#     if row[3] > 150:
#         print(row[3])

# 197
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# for row in ohlc[1:]:
#     if row[3] >= row[0]:
#         print(row[3])

# 198
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# volatility = []
# for row in ohlc[1:]:
#     band = row[1] - row[2]
#     volatility.append(band)
# print(volatility)

# 199
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# for row in ohlc[1:]:
#     band = row[1] - row[2]
#     if row[3] > row[0]:
#         print(band)

# 200   !!
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# total_rate = []
# for row in ohlc[1:]:
#     rate = row[0] - row[3]
#     total_rate.append(rate)
# print(sum(total_rate))
#
# profit = 0
# for row in ohlc[1:]:
#     profit += row[0] - row[3]
# print(profit)

