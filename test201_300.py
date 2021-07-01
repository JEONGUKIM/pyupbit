#### 파이썬 함수(201~240), 파이썬 모듈(241~250), 파이썬 클래스(251~290) #######

# 201
# def print_coin():
#     print("비트코인")
# print_coin()

# 202
# def coin():
#     print("비트코인")
# coin()

# 203
# for i in range(100):
#     coin()

# 204   !!
# def coin():
#     for i in range(100):
#         print("비트코인")
# coin()

# 205
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
# def smile():
#     data = input("입력: ")
#     print(data + ":D")
#
# smile()
#
# def with_smile(string):
#     print(string + ":D")
#
# with_smile(크크크)

# 216
# def with_smile(string):
#     print(string + ":D")
#
# with_smile("안녕하세요")

# 217
# def price(current_price):
#     print(current_price * 1.3)
#
# price(10000)

# 218
# def sum(a, b):
#     print(a + b)
# sum(1, 3)

# 219
# def operation(a, b):
#     print(f"{a} + {b} = {a + b}" )
#     print(f"{a} - {b} = {a - b}")
#     print(f"{a} * {b} = {a * b}")
#     print(f"{a} / {b} = {a / b}")
#
# operation(3, 4)

# 220
# def maxx(a, b, c):
#     if a > b and a > c:
#         print(a)
#     elif b > a and b > c:
#         print(b)
#     else:
#         print(c)
# maxx(1, 2, 3)

# # 221
# def reverse(string):
#     print(string[::-1])
#
# reverse("good")

# 222       !!
# def score(grade):
#     print(sum(grade) / len(grade))
#
# score([1, 2, 3])

# 223
# def even(list):
#     for i in list:
#         if i % 2 == 0:
#             print(i)
# even ([1, 3, 2, 10, 12, 11, 15])

# 224
# def print_keys(list):
#     for i in list:      # for i in list.keys() 해도 상관없음, 기본적으로 keys함수를 안쓰면 키값만 출력
#         print(i)
#
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
#
# def by_key(a, b):
#     print(my_dict[b])
#
# by_key(my_dict, "10/26")

# 226   !!
# def print_5xn(string):
#     times = len(string) / 5
#     times = int(times + 0.9)
#
#     for i in range(times):
#         print(string[5*i : 5*i+5])
#
# print_5xn("아이엠어보이유알아걸맨아이러브유오예스")

# 227   !!
# def printmxn(string, num):
#     times = len(string) / num
#     times = int(times + 0.9)
#
#     for i in range(times):
#         print(string[i*num : i * num + num])
#
# printmxn("아이엠어보이유알어걸", 3)

# 228
# def salary(good):
#      print(int(good / 12))
#
# salary(12000000)


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

# 232   !!
# def make_url(string):
#    domain = "www." + string + ".com"
#    return domain
#
# result = make_url("naver")
# print(result)

# 233
# def make_list(data):
#     return list(data)
#
# result = make_list("abcd")
# print(result)

# 234
# def pickup_even(data):
#     list = [ ]
#     for i in data:
#         if i % 2 == 0:
#             list.append(i)
#     return list
#
# result = pickup_even([3, 4, 5, 6, 7, 8])
# print(result)

# 235   !!
# def convert_int(data):
#     return int(data.replace(",", ""))
#
# result = convert_int("1,234,567")
# print(result)

# 236
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

#### 파이썬 모듈 #####
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

# 243   !!
# import datetime
#
# now = datetime.datetime.now()
# for i in range(-5, 0):      # range(5, 0, -1) 같다.
#     delta = datetime.timedelta(i)
#     date = now - delta
#     print(date)

# 244   !!
# import datetime
#
# now = datetime.datetime.now()
# print(now.strftime("%H:%M:%S"))

# 245   !!
# import datetime
#
# day = "2020-05-04"
# ret = datetime.datetime.strptime(day, "%Y-%m-%d")
# print(ret, type(ret))

# 246
# import datetime
# import time
#
# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

# 247

# 248
# import os
#
# ret = os.getcwd()
# print(ret, type(ret))

# 249
# import os
#
# os.rename("C:/Users/user/Desktop/aa.txt", "C:/Users/user/Desktop/bb.txt")


# 250
# import numpy
#
# for i in numpy.arange(0, 5.1, 0.1):
#     print(i)

####### 파이썬 클래스 #####
# 251
# 붕어빵틀 = 클래스
# 붕어빵 = 객체, 오브젝트, 인스턴스

# 252
# class Human:
#     pass

# 253
# class Human:
#     pass
# areum = Human()

# 254
# class Human:
#     def __init__(self):
#         print("응애응애")
#
# areum = Human()

# 255
# class Human:
#     def __init__(self, name, age, sex):
#         self.name, self.age, self.sex = name, age, sex
#
# areum = Human("아름", 25, "여자")
# print(areum.name)

# 256
# class Human:
#     def __init__(self, name, age, sex):
#         self.name, self.age, self.sex = name, age, sex
#
# areum = Human("아름", 25, "여자")
# print(areum.age)

# 257
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def who(self):
#         print(f"이름: {self.name}, 나이:{self.age}, 성별:{self.sex}")
#
# areum = Human("아름", 25, "여자")
# areum.who()

# 258
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def who(self):
#         print(f"이름: {self.name}, 나이:{self.age}, 성별:{self.sex}")
#
#     def setinfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# areum = Human("모름", 0, "모름")
# areum.who()
#
# areum.setinfo("아름", 25, "여자")
# areum.who()

# 259
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __del__(self):
#         print("나의 죽음을 알리지 말라")
#
#     def who(self):
#         print(f"이름: {self.name}, 나이:{self.age}, 성별:{self.sex}")
#
#     def setinfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# areum = Human("아름", 25, "여자")
# del areum

# 260
# class OMG :
#     def print() :
#         print("Oh my god")
#
# myStock = OMG()
# myStock.print()

# 261
# class Stock:
#     pass

# 262
# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code
#
# 삼성 = Stock("삼성전자", "005930")
# print(삼성.name)
# print(삼성.code)

# 263
# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code
#
#     def set_name(self, name):
#         self.name = name
#
# a = Stock(None, None)
# a.set_name("삼성전자")
# print(a.name)
# print(a.code)

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
# a.set_name("삼성전자")
# a.set_code("005930")
# print(a.name)
# print(a.code)

# 265   !!
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
# print(삼성.get_name())
# print(삼성.get_code())

# 266
# class Stock:
#     def __init__(self, name, code, PER, PBR, rate):
#         self.name = name
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.rate = float(rate)
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
#     def __init__(self, name, code, PER, PBR, rate):
#         self.name = name
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.rate = rate
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
# sam = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# print(sam.rate)

# 268
# class Stock:
#     def __init__(self, name, code, PER, PBR, rate):
#         self.name = name
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.rate = rate
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
#     def set_per(self, PER):
#         self.PER = PER
#     def set_pbr(self, PBR):
#         self.PBR = PBR
#     def set_rate(self, rate):
#         self.rate = rate

# 269
# class Stock:
#     def __init__(self, name, code, PER, PBR, rate):
#         self.name = name
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.rate = rate
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
#     def set_per(self, PER):
#         self.PER = PER
#     def set_pbr(self, PBR):
#         self.PBR = PBR
#     def set_rate(self, rate):
#         self.rate = rate
#
# sam = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# sam.set_per(12.75)
# print(sam.PER)

# 270
# class Stock:
#     def __init__(self, name, code, PER, PBR, rate):
#         self.name = name
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.rate = rate
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
#     def set_per(self, PER):
#         self.PER = PER
#     def set_pbr(self, PBR):
#         self.PBR = PBR
#     def set_rate(self, rate):
#         self.rate = rate
#
# s = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# h = Stock("현대차", "005380", 8.70, 0.35, 4.27)
# l = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
# list = []
# list.append(s)
# list.append(h)
# list.append(l)
#
# for i in list:
#     print(i.code, i.PER)

# 271   !!
# import random
#
# class Account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_num = num1 + "-" + num2 + "-" + num3
#
# kim = Account("김철수", 10000)
# print(kim.name)
# print(kim.balance)
# print(kim.bank)
# print(kim.account_num)

# 272   !!
# import random
#
# class Account:
#     account_count = 0       # 클래스 변수
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_num = num1 + "-" + num2 + "-" + num3
#
#         Account.account_count += 1
#
# kim = Account("김민수", 100)
# print(Account.account_count)
# lee = Account("이민수", 100)
# print(Account.account_count)

# 273
# import random
#
# class Account:
#     account_count = 0       # 클래스 변수
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_num = num1 + "-" + num2 + "-" + num3
#
#         Account.account_count += 1
#
#     @classmethod       # 객체에서 불어오는게아니라, 클래스공간에서 불러오는것이므로, self를 받을 필요가없다.
#     def get_account_num(cls):    # cls 자리에 호출한 객체가 들어가는게 아니라, 클래스의 이름이 들어간다.
#         print(cls.account_count)
#
# kim = Account("김민수", 100)
# lee = Account("이민수", 100)
# kim.get_account_num()

# 274
# import random
#
# class Account:
#     account_count = 0       # 클래스 변수
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_num = num1 + "-" + num2 + "-" + num3
#
#         Account.account_count += 1
#
#     @classmethod       # 객체에서 불어오는게아니라, 클래스공간에서 불러오는것이므로, self를 받을 필요가없다.
#     def get_account_num(cls):    # cls 자리에 호출한 객체가 들어가는게 아니라, 클래스의 이름이 들어간다.
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount > 0 :
#             self.balance += amount

# kim = Account("김민수", 10000)
# print(kim.balance)
# kim.deposit(1000)
# print(kim.balance)

# 275
# import random
#
# class Account:
#     account_count = 0       # 클래스 변수
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_num = num1 + "-" + num2 + "-" + num3
#
#         Account.account_count += 1
#
#     @classmethod       # 객체에서 불어오는게아니라, 클래스공간에서 불러오는것이므로, self를 받을 필요가없다.
#     def get_account_num(cls):    # cls 자리에 호출한 객체가 들어가는게 아니라, 클래스의 이름이 들어간다.
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount > 0 :
#             self.balance += amount
#
#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount


# kim = Account("김민수", 10000)
# print(kim.balance)
# kim.withdraw(1000)
# print(kim.balance)

# 276
# import random
#
# class Account:
#     account_count = 0       # 클래스 변수
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_num = num1 + "-" + num2 + "-" + num3
#
#         Account.account_count += 1
#
#     @classmethod       # 객체에서 불어오는게아니라, 클래스공간에서 불러오는것이므로, self를 받을 필요가없다.
#     def get_account_num(cls):    # cls 자리에 호출한 객체가 들어가는게 아니라, 클래스의 이름이 들어간다.
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount > 0 :
#             self.balance += amount
#
#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름:", self.bank)
#         print("예금주:", self.name)
#         print("계좌번호:", self.account_num)
#         print("잔고: {:,}".format(self.balance))

# kim = Account("김철수", 10000)
# kim.display_info()

# 277
# import random
#
# class Account:
#     account_count = 0       # 클래스 변수
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0      # 계좌생성시 생성자에서 계좌별로 만들어져서 따로 카운트해야하므로, 생성자안에 만든다.
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_num = num1 + "-" + num2 + "-" + num3
#
#         Account.account_count += 1
#
#         deposit_count = 0
#
#     @classmethod       # 객체에서 불어오는게아니라, 클래스공간에서 불러오는것이므로, self를 받을 필요가없다.
#     def get_account_num(cls):    # cls 자리에 호출한 객체가 들어가는게 아니라, 클래스의 이름이 들어간다.
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount > 0 :
#             self.balance += amount
#
#             # 5회마다 이자 지급
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:
#                 self.balance = self.balance * 1.01
#
#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름:", self.bank)
#         print("예금주:", self.name)
#         print("계좌번호:", self.account_num)
#         print("잔고: {:,}".format(self.balance))
#
# kim = Account("김철수", 1000)
# lee = Account("이영희", 1000)
# kim.deposit(1000)
# kim.deposit(1000)
# kim.deposit(1000)
# kim.deposit(1000)
# kim.deposit(1000)
# kim.deposit(1000)
# kim.deposit(1000)
# kim.deposit(1000)
# kim.deposit(1000)
# kim.deposit(1000)
#
# print(kim.balance)
# print(lee.balance)

# 278
# import random
#
# class Account:
#     account_count = 0       # 클래스 변수
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0      # 계좌생성시 생성자에서 계좌별로 만들어져서 따로 카운트해야하므로, 생성자안에 만든다.
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_num = num1 + "-" + num2 + "-" + num3
#
#         Account.account_count += 1
#
#         deposit_count = 0
#
#     @classmethod       # 객체에서 불어오는게아니라, 클래스공간에서 불러오는것이므로, self를 받을 필요가없다.
#     def get_account_num(cls):    # cls 자리에 호출한 객체가 들어가는게 아니라, 클래스의 이름이 들어간다.
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount > 0 :
#             self.balance += amount
#
#             # 5회마다 이자 지급
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:
#                 self.balance = self.balance * 1.01
#
#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름:", self.bank)
#         print("예금주:", self.name)
#         print("계좌번호:", self.account_num)
#         print("잔고: {:,}".format(self.balance))
#
# kim = Account("김철수", 1000)
# lee = Account("이영희", 1000)
# park = Account("박수진", 1000)
# list = []
# list.append(kim)
# list.append(lee)
# list.append(park)
# print(list)

# 279
# import random
#
# class Account:
#     account_count = 0       # 클래스 변수
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0      # 계좌생성시 생성자에서 계좌별로 만들어져서 따로 카운트해야하므로, 생성자안에 만든다.
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_num = num1 + "-" + num2 + "-" + num3
#
#         Account.account_count += 1
#
#         deposit_count = 0
#
#     @classmethod       # 객체에서 불어오는게아니라, 클래스공간에서 불러오는것이므로, self를 받을 필요가없다.
#     def get_account_num(cls):    # cls 자리에 호출한 객체가 들어가는게 아니라, 클래스의 이름이 들어간다.
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount > 0 :
#             self.balance += amount
#
#             # 5회마다 이자 지급
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:
#                 self.balance = self.balance * 1.01
#
#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름:", self.bank)
#         print("예금주:", self.name)
#         print("계좌번호:", self.account_num)
#         print("잔고: {:,}".format(self.balance))
#
# list = []
# kim = Account("김정우", 1000000000000)
# lee = Account("이영희", 1000)
# park = Account("박수진", 10000000)
#
# list.append(kim)
# list.append(lee)
# list.append(park)
#
# for i in list:
#     if i.balance >= 1000000:
#         print("{}, {:,}".format(i.name, i.balance))

# 280
# import random
#
# class Account:
#     account_count = 0       # 클래스 변수
#
#     def __init__(self, name, balance):
#         self.deposit_count = 0      # 계좌생성시 생성자에서 계좌별로 만들어져서 따로 카운트해야하므로, 생성자안에 만든다.
#         self.deposit_log = []
#         self.withdraw_log = []
#
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)
#
#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_num = num1 + "-" + num2 + "-" + num3
#
#         Account.account_count += 1
#
#         deposit_count = 0
#
#     @classmethod       # 객체에서 불어오는게아니라, 클래스공간에서 불러오는것이므로, self를 받을 필요가없다.
#     def get_account_num(cls):    # cls 자리에 호출한 객체가 들어가는게 아니라, 클래스의 이름이 들어간다.
#         print(cls.account_count)
#
#     def deposit(self, amount):
#         if amount > 0 :
#             self.deposit_log.append(amount)
#             self.balance += amount
#
#             # 5회마다 이자 지급
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:
#                 self.balance = self.balance * 1.01
#
#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.withdraw_log.append(amount)
#             self.balance -= amount
#
#     def display_info(self):
#         print("은행이름:", self.bank)
#         print("예금주:", self.name)
#         print("계좌번호:", self.account_num)
#         print("잔고: {:,}".format(self.balance))
#
#     def deposit_history(self):
#         for amount in self.deposit_log:
#             print(amount)
#
#     def withdraw_history(self):
#         print(self.withdraw_log)
#
# kim = Account("김철수", 10000)
# kim.deposit(10000)
# kim.deposit(10000)
# kim.deposit_history()
# kim.withdraw(1000)
# kim.withdraw_history()
# print(kim.balance)

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
#     pass

# 283   !!
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
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#         self.구동계 = 구동계
#
# bicycle = 자전차(2, 100, "시마노")
# print(bicycle.구동계)
#
#
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         super().__init__(바퀴, 가격)     # 부모클래스에 같은게 있으므로 다시 안만들고, 부모클래스를 활용.
#         self.구동계 = 구동계
#
# bicycle = 자전차(2, 100, "시마노")
# print(bicycle.구동계)

# 285
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         super().__init__(바퀴, 가격)     # 부모클래스에 같은게 있으므로 다시 안만들고, 부모클래스를 활용.
#         self.구동계 = 구동계
#
# class 자동차(차):
#     def __init__(self, 바퀴, 가격):
#         super().__init__(바퀴, 가격)
#
#     def 정보(self):
#         print("바퀴수:", self.바퀴)
#         print("가격:", self.가격)
#
# car = 자동차(4, 1000)
# car.정보()

# 286
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#
#     def 정보(self)                    # 상송클래스에 중복되는 함수가 생기므로, 부모클래스에 만들어서 사용한다.
#         print("바퀴수:", self.바퀴)
#         print("가격:", self.가격)
#
# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         super().__init__(바퀴, 가격)     # 부모클래스에 같은게 있으므로 다시 안만들고, 부모클래스를 활용.
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
#     def 정보(self):                   # 상송클래스에 중복되는 함수가 생기므로, 부모클래스에 만들어서 사용한다.
#         print("바퀴수:", self.바퀴)
#         print("가격:", self.가격)
#
# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         super().__init__(바퀴, 가격)          # 부모클래스에 같은게 있으므로 다시 안만들고, 부모클래스를 활용.
#         self.구동계 = 구동계
#
#     def 정보(self):
#         super().정보()                # 부모클래스 함수 불러와서 사용
#         print("구동계:", self.구동계)
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

# 290
# class 부모:
#   def __init__(self):
#     print("부모생성")
#
# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
#     super().__init__()
#
# 나 = 자식()

print("정말정말 여기까지 공부하느냐 수고 많으셨습니다. ^^")
print("앞으로 10 문제만 풀면 '300'제 수업이 끝납니다. 화이팅!!!!!! ^^")
print("문법은 공부안하고 시간이지나면 까먹을 수 있으니, 틈날때마다 복습 해주세요~~")

####### 파일 입출력과 예외처리 ###########
# 291
