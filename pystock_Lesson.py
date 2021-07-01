

# While문 연습문제

# 1. while 문을 사용하여 10,000 원에서 5일연속 상한가(30%)를 기록한 경우의 금액을 출력하세요.
# price = 10000
# day = 1
#
# while day <= 5:
#     price = price * 1.3
#     print(day, price)
#     day += 1
#
# print("최종금액:", price)


# 2. 로또번호 1-45의 숫자 6개를 생성해보세요. (숫자중복없음) /
#     import random   # 모듈import는 한번만
#     number = random.randint(1, 45)  # 숫자를 만들때마다 호출

import random

# lotto =[]
# while len(lotto) != 6:
#     num = random.randint(1, 45)
#     if num not in lotto:
#         lotto.append(num)
# print(lotto)


# count = 0
# lotto = []
# while count < 6:
#     num = random.randint(1, 45)
#     if num not in lotto:
#         lotto.append(num)
#         count += 1
#
# print(lotto)

# 강의

##################### 결과값이 있는 함수 #######################
# def mysum(a,b):
#     val = a +b
#     return val
#
# ret = mysum(30, 40)     # 리턴값이 있는함수는 항상 왼쪽에 변수를 입력해 줘야한다.
#
# print(ret)

# def average(a, b):
#     평균 = (a + b) / 2
#     return 평균
#
# ret = average(10, 20)
# print(ret)

# def mymax(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# ret = mymax(30, 4)
# print(ret)

# def coin(ticker):
#     coin_name = ticker[:3]
#     return coin_name
#
# ret = coin("XRP-KRW")
# print(ret)

# def myaverage(ave):
#     average = sum(ave) / len(ave)
#     return average
#
# ret = myaverage([1, 2, 3])
# print(ret)

# LEGB 순서
# global함수를 이용해서 함수 바깥에있는 값을 수정 할 수 있다.
# a = 10
#
# def test():
#     global a
#     a = 20
#
# test()
# print(a)

# 리스트, 딕셔너리를 사용할때는 global함수를 사용하지않아도, 함수내에서 리스트에 접금해서 값을 수정 할 수 있다.
# data = [10, 20, 30]
#
# def mul10(data_list):
#     data_list[0] = data_list[0] * 10
#
# mul10(data)
# print(data)

##################### 모 듈 #######################

# 파이썬 파일이 모듈(함수의 묶음)이다. test.py -> test 모듈
# 모듈은 다른말로 라이브러리 라고 함.

# ex1. 날짜와 시간을 다루는 모듈
# import datetime
#
# cur_time = datetime.datetime.now()
# print(cur_time, type(cur_time))
# time = str(cur_time)
# print(time, type(time))
# print(time[:10])


# 현재시간으로부터 하루 뒤 datetime.timedelta()
# import datetime
# now = datetime.datetime.now()
# tomorrow = now + datetime.timedelta(days=1)     # days= 안적어도 된다. 숫자만 적어도됨. / minutes=100, 100분뒤가된다.
# print(tomorrow)

# ex2. time모듈
# import time
#
# print("Hello")
# time.sleep(5)
# print("Good bye")

# 1초에 한번씩 현재시간을 출력
# import time
# import datetime
#
# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

# ex.3 OS모듈
# os모듈은 운영체제와 관련된 여러가지 기능을 제공하는 모듈
# import os
#
# ret = os.listdir("C:/")
#
# for i in ret:
#     print(i)

# ex4. 그래프 그리기 모듈. matplotlib
# import matplotlib.pyplot as plt     # matplotlib 디렉토리안에있는 pyplot모듈을 사용한다.  plt로 정의해서
#
# plt.plot([1, 2, 3, 4])
# plt.show()

# 나만의 모듈 만들기

''''#### 클래스 #####'''
'''
붕어빵틀 = 클래스(class)
붕어빵 = 객체, 오브젝트, 인스턴스
속성 = property(변수), method(함수)
'''

# 클래스 상속

# class parent:
#     def sing(self):
#         print("sing a song")
#
# class LuckyChild(parent):
#     def dance(self):
#         print("shuffle dance")
#
# luckyboy = LuckyChild()
# luckyboy.sing()
# luckyboy.dance()

# 연습문제 1
# class 통장:
#     def __init__(self, 이름, 잔고):
#         self.이름, self.잔고 = 이름, 잔고
#
#     def 입금(self, 입금액):
#         self.잔고 += 입금액      # self.잔고 = self.잔고 + 입금액
#         print(입금액, "이 입급되었습니다.")
#
#     def 출금(self, 출금액):
#         if 출금액 > self.잔고:
#             print("잔고부족")
#         else:
#             self.잔고 -= 출금액
#             print(출금액, "이 출금되었습니다.")
#
# 계좌 = 통장("정우", 10000)
# print(계좌.잔고)
# 계좌.입금(10000)
# print(계좌.잔고)
# 계좌.출금(30000)
# 계좌.출금(15000)
# print(계좌.잔고)

# 연습문제 2 (연습문제 1번과 연계, 상속)
# class 마이너스통장(통장):
#     def 출금(self, 출금액):
#         self.잔고 -= 출금액
#         print(출금액, "이 출금되었습니다.")
#
# 정우 = 마이너스통장("정우", 10000)    # 마이너스통장으로 클래스를 호출해도 부모클래스(통장)에 있는 매서드를 사용할 수 있다.
# print(정우.잔고)
#
# 여러분 = 통장("여러분", 10000)
# 내통장 = 마이너스통장("내통장", 10000)
#
# print(여러분.잔고, 내통장.잔고, 정우.잔고)
# 여러분.출금(20000)
# 내통장.출금(20000)
# print(내통장.잔고)

''''#### 파일다루기 #####'''
# 인코딩 : 한글, 영어 의 문자들이 파일로 저장될때 숫자로 변환되는 것.
# 디코딩 : 반대로 인코딩으로 저장되어있걸 불러오는걸 디코딩 이라 부른다.
# 우리나라는 기본 웹페이지 형식으로 UTF-8 을 사용한다.
# 윈도우는 기본적으로 CP949 로 인코딩 되어있다.

# 파이썬으로 파일 읽기
'''
1. 파일읽기 - open 함수
2. 데이터읽기 - readlines 함수
3. 파일닫기 - close함수

파일을열때는 경로명에 C:\a\b\c 기본적으로 이렇게되지만 역슬러쉬를 파이썬에서는 다른 의미로 사용하기때문에
이 '/' 슬러쉬를 사용해줘야한다. 아니면, 역슬러쉬를 2번 '\\' 해주면 된다. 
'''

# a = open("C:\\Users\\user\\Desktop\\buy_list.txt", encoding="utf-8")
# line = a.readlines()
# a.close()
#
# for i in line:
#     print(i.strip())

# 파이썬으로 파일로 쓰기
'''
1. 파일열기 - open함수
2. 데이터 쓰기 - write함수
3. 파일닫기 - close함수     
 ** 쓰기할때는  꼭 close함수로  닫아줘야한다 !!! 중요!!
 ** 파일열때 경로명 과 인코딩 내용 사이에 "wt" 라고 넣어줘야한다. 안그러면 기본적으로 읽기모드가 된다.
'''

# a = open("C:\\Users\\user\\Desktop\\buy_list.txt", "wt", encoding="utf-8")
# a.write("나는 1조 부자입니다.\n나는 완전히 경제적인 자유를 이루었습니다.")
# a.close()

##### 예외 처리 ##############
# 예외(exception): 프로그램이 실행중 발생하는 에러
# 파이썬에서는 try~ except 구문을 통해서 예외를 처리함.

# data_list = ["1.0", "2.0", ""]
# for i in data_list:
#     data = float(i)     # 마지막 "" 비어있는값이 들어올때 에러가 발생
#     print(data)

# 수정 (예외처리)
# data_list = ["1.0", "2.0", ""]
# for i in data_list:
#     try:
#         data = float(i)
#     except:
#         data = 0    # 에러발생시 값을 어떻게 처리할지.
#     print(data)


########################### 판다스 ##################################################################################

###### numpy 기초 ########
# import numpy as np

# data = [1, 2, 3, 4]
# result = []
#
# for i in data:
#     result.append(i*10)
#
# print(result)

# import numpy as np
#
# a = np.array([1, 2, 3, 4])      # for문을 사용하지 않고도, 리스트값에 똑같이 10을 곱해줄 수 있다.
# b = a * 10
# print(b, type(b))

# 2차원 데이터(1/2)
''' 
 -  리스트로 2차원 데이터를 표현하기.
 - 데이터를 행 단위로 구성하는 경우, 열단위로 접근할 수가 없음.(그 반대도 마찬가지)
    (for문을 사용해서 가져올 수 는 있지만, 일반적인 방법으로는 가져올수없다.) 
    
고가   시가   저가   종가
100    80    70     90
120    110   100   110
'''

# price = [
#     [100, 80, 70, 90],
#     [120, 110, 100, 110]
# ]
# print(price)

# 2차원 데이터(2/2)
# import numpy as np
#
# price = [
#     [100, 80, 70, 90],
#     [120, 110, 100, 110]
# ]
#
# a = np.array(price)
# print(a, type(a))
# print(a[0])
# print(a[1])
# print()
#
# # 넘파이 인덱싱 (두 개다 같은 방법임.)
# print(a[0][0])  # 특정 값에 접근할때, 행(몇층인지) -> 열(몇호인지) 순서로 접근 / 방법1
# print(a[1,0])   # 특정 값에 접근할때, 행(몇층인지) -> 열(몇호인지) 순서로 접근 / 방법2
#
# # 넘파이 슬라이싱
# print(a[:, 0])      # 행은 모든것, 열은 0번 것.
# print(a[0, :])      # 0번째 행의, 모든 것.  = a[0]


###### series 생성 ########

'''
 - Pandas 기본 자료 구조
 Series : numpy 를 기반으로 만들어진 1차원 데이터를 위한 자료구조.
 DataFrame : numpy 를 기반으로 만들어진 2차원 데이터를 위한 자료구조.
'''

'''
 - 임포트 방식
 1. form pandas import Series(또는 DataFrame)
        series()
        DataFrame()
    
 2. import pandas as pd
        pd.Series()
        pd.DataFrame()
'''

# Series 객체 생성
# from pandas import Series
#
# arr = [0, 1, 2, 3]
# s = Series(arr)
# print(s)    # 출력 첫번째가 행번호(보이지 않는다.), 그다음 인덱스번호(출력화면 첫번째 열), 그다음 열에 출력되는것이 입력된 데이터

# Series 내부구조.
# from pandas import Series
#
# data = [100, 200, 300]
# s = Series(data)
# print(s)        # 첫 열의 인덱스 번호는 수정 할 수 있다. / 인덱스 번호와 데이터는 수정할 수 있지만, 행번호는 수정할 수 없다.


# from pandas import Series

# data1 = [100, 200, 300]
# day = ["월", "화", "수"]       # 인덱스 수정
# s1 = Series(data1, day)      # Series(data=data1, index=day) 와 같다.
# print(s1)

'''
 -  출력 결과(개념)
 행번호(보이지않음)      인덱스     데이터
    0                  "월"      100
    1                  "화"      200
    2                  "수"      300
    
이렇게 표현이 된다.   (행번호가 꼭 0번부터 순서대로 안 나오는것도 있다. 알고만 있자.)
'''

# Series 속성
# from pandas import Series
#
# data1 = [100, 200, 300]
# day = ["월", "화", "수"]       # 인덱스 수정
# s1 = Series(data1, day)      # Series(data=data1, index=day) 와 같다.
# print(s1.index)             # 시리즈 객체의 인덱스를 접근   /  판다스에서 object 라는 것은 문자열로 인식한다는 의미이다.
# print(s1.values)            # 시리즈 객체의 값에 접근    /    호출을 의미하는 () 는 써줄 필요 없다(메소드가 아니기때문에).


#### 연습문제1
'''
 - 다음 데이터를 판다스 시리즈(Series) 객체로 생성하세요.
index       value
메로나         500
누가바         800
빠삐코         200
'''

# from pandas import Series
#
# ice = [500, 800, 200]
# ice_name = ["메로나", "누가바", "빠삐코"]
# ice_info = Series(data=ice, index=ice_name)
# print(ice_info)

##### 시리즈 인덱싱 / 슬라이싱 방법 #######

##### 인덱싱 ####
'''
Series 인덱싱 (1/3)
iloc 속성(변수)을 사용하여 인덱싱
시리즈 객체의 '행번호' 를 사용하여 인덱싱

즉, iloc는 행번호를 사용해서 인덱싱한다.
'''
# from pandas import Series
#
# data1 = [100, 200, 300]
# day = ["월", "화", "수"]       # 인덱스 수정
# s1 = Series(data1, day)
# print(s1.iloc[0])   # 시리즈 객체의 행번호 입력 -> value 값 출력
# print(s1.iloc[2])   # = iloc[-1] 같다. /  맨뒤에서부터 -1, -2.. 순서로도 인덱싱 가능

'''
Series 인덱싱 (2/3)
loc 속성 사용
시리즈 객체의 '인덱스'를 사용하여 인덱싱
'''
# from pandas import Series
#
# data1 = [100, 200, 300]
# day = ["월", "화", "수"]       # 인덱스 수정
# s1 = Series(data1, day)
# print(s1.loc["월"])   # 시리즈 객체의 인덱스 입력 -> value 값 출력
# print(s1.loc["화"])

'''
Series 인덱싱 (3/3)
대괄호([]) 를 사용하여 인덱싱
'''
# from pandas import Series
#
# data1 = [100, 200, 300]
# day = ["월", "화", "수"]
# s1 = Series(data1, day)
# print(s1[1])   # 기본적으로 대괄호[] 안에 인덱스 값을 입력하면 되지만, 최근 버전에서는 행번호를 입력해도 됨.
# print(s1["수"])  # 대괄호 인덱싱보다는 , iloc나 loc를 써줘서 명확하게 해주는게 더 좋다(개인마다 다름)

#### 슬라이싱 ####

'''
Series 슬라이싱 (1/2)
행번호를 사용하여 슬라이싱
iloc 사용(행단위로 출력) - 기본적으로 리스트 슬라이싱처럼 개념적용 맨처음 값 전이 0, 1, 2, 순번으로 (행을기준으로 적용하면된다.)
'''
# from pandas import Series
#
# data1 = [100, 200, 300]
# day = ["월", "화", "수"]
# s1 = Series(data1, day)
# print(s1.iloc[0:2])     # 새로운 시리즈객체 형태로 출력된다.

'''
Series 슬라이싱 (2/2)
loc 사용
끝인덱스 포함. 
loc[시작인덱스:끝인덱스]
'''
# from pandas import Series
#
# data1 = [100, 200, 300]
# day = ["월", "화", "수"]
# s1 = Series(data1, day)
# print(s1.loc["월":"화"])     # 새로운 시리즈객체 형태로 출력된다.

'''
여러 값 인덱싱
연속적이지 않은 여러개의 값을 한번에 인덱싱
행번호 또는 인덱스를 파이썬 리스트로 구성함
iloc(행기준), loc(인덱스 기준) 속성에서 해당 리스트를 사용
'''
# from pandas import Series
#
# data1 = [100, 200, 300]
# day = ["월", "화", "수"]
# s1 = Series(data1, day)
# # target = [0, 2]     # 행번호(iloc)사용 또는 인덱스(loc 사용) 할 리스트 구성
# # print(s1.iloc[target])
# print(s1.iloc[[0, 2]])      # 위 2줄(target 리스트만들지않고) 바로 이렇게 표현할수있다.

# from pandas import Series
#
# data1 = [100, 200, 300]
# day = ["월", "화", "수"]
# s1 = Series(data1, day)
# print(s1.loc[["월", "수"]])

######### Series 추가, 삭제, 수정 #################

## Series에 값 추가
'''
딕셔너리와 유사한 방식으로 값 추가 가능
s.loc[인덱스] = 값
'''
# from pandas import Series
#
# data = [100, 200, 300]
# day = ["월", "화", "수"]
# s = Series(data, day)
# print(s)
# s.loc["목"] = 400
# print(s)


### Series 삭제
'''
drop 메서드
원본은 유지하고 값이 삭제된 시리즈 객체를 리턴
s.drop("인덱스")
s.drop(["인덱스1", "인덱스2"])   여러개 선택해서  삭제  가능
'''
# from pandas import Series
#
# data = [100, 200, 300]
# day = ["월", "화", "수"]
# s = Series(data, day)
#
# s1 = s.drop("월")    # 원본은 그대로이므로 다른 변수에 값을 바인딩시켜줌 / s.drop(인덱스, inplace=True) 해주면 원본에 바로 적용.
# print(s1)


### Series 수정
'''
딕셔너리 와 유사
행번호나 인덱스를 사용하여 value를 수정
'''
# from pandas import Series
#
# data = [100, 200, 300]
# day = ["월", "화", "수"]
# s = Series(data, day)


# s.iloc[0] = 1000
# s.loc["수"] = 3000
# print(s)


###########  Series 연산 #####################

## 브로드캐스팅
# from pandas import Series
#
# s = Series([100, 200, 300])
# print(s + 10)   # 모든 값에 10을 각각 더한 값이 출력된다.

## 사칙연산(1/2)
# from pandas import Series
#
# high = Series([51500, 51200, 52500, 51500, 51500])
# low = Series([50700, 50500, 50500, 50800, 50700])
# diff = high - low
# print(diff)

## 사칙연산(2/2)
# from pandas import Series
#
# high = Series(data=[51500, 51200, 52500], index=["5/1", "5/2", "5/3"])
# low = Series(data=[50700, 50500, 50500], index=["5/1", "5/2", "5/4"])
# diff = high - low
# print(diff)     # 5/3 인덱스에서 뺄 같은 인덱스가 없으므로 NaN(Not a Number) 출력, 5/4일도 NaN

## 시리즈 비교 연산
# from pandas import Series
#
# s = Series(data=[100, 200, 300, 400, 500])
# cond = s > 300
# print(cond)      ## 불린 형태의 시리즈 객체형태로 출력

## 시리즈 필터링(1/2)
'''True/False 값을 통해서 True 값만 필터링 가능'''
# from pandas import Series
#
# s = Series(data=[100, 200, 300, 400, 500])
# cond = [False, False, False, True, True]
# print(s[cond])      # False 를 제외한 True에 상응하는 value 값만 새로운 시리즈 객체 형태로 출력

## 시리즈 필터링(2/2)
# from pandas import Series
#
# s = Series(data=[100, 200, 300, 400, 500])
# cond = s > 300
# print(s[cond])      # 300보다 작은 값에 해당되는 True 값만 새로운 시리즈 객체형태로 출력

## 시리즈 필터링 연습
# 시가가 300원 이상인 날의 종가를 출력

# from pandas import Series
#
# open = Series(data=[100, 200, 300, 400, 600])
# close = Series(data=[100, 300, 400, 500, 600])
#
# condition = open >= 300
# print(close[condition])

## 연습문제 1
# 고가와 저가 차이가 100이상인 날의 고가를 출력하세요
# from pandas import Series
#
# low = Series([10, 200, 200, 400, 600])
# high = Series([100, 300, 400, 500, 600])
#
# condition = (high - low) >= 100
# print(high[condition])

## 연습문제 2
# 종가가 80000원 이상 90000원 미만인 날짜를 출력하라
# from pandas import Series
#
# close = Series([93000, 82400, 99100, 81000, 72300],
#                ["05/14", "05/15", "05/16", "05/17", "05/18"])
#
# condition = (close >= 80000) & (close < 90000)      # and 를 시리즈에서는 & 로 표현
# s = close[condition]
# print(s.index)
#
# for i in s.index:
#     print(i)

################## DataFrame 생성 ######################

## DataFrame 생성(1/3)
'''
2차원 표에서 컬럼 단위로 데이터를 표현
컬럼명을 딕셔너리의 key로, 데이터는 딕셔너리의 value로 사용
'''

# from pandas import DataFrame
#
# stock = {
#     "종가": [157000, 51300, 68800, 140000],
#     "PER": [39.88, 8.52, 10.03, 228.38],
#     "PBR": [4.38, 1.45, 0.87, 2.16]
# }
#
# name = ["NAVER", "삼성전자", "LG", "카카오"]
#
# df = DataFrame(data=stock, index=name)
# print(df)


## DataFrame 생성(2/3)
'''
2차원 표에서 로우 단위로 데이터를 리스트로 표현
data, index, columns를 각각 리스트로 표현
* 일반적으로 어떤주식의 정보가 들어오고 그다음주식.. 이런식으로 데이터가 들어오는경우 이 방법을 많이쓴다.
   가끔씩 컬럼단위로 정보가 들올경우에는 위에 1번방식으로 하는게 편할 수 있다.
'''

# from pandas import DataFrame
#
# stock = [
#     [157000, 39.88, 4.38],
#     [51300, 8.52, 1.45],
#     [68800, 10.03, 0.87],
#     [140000, 228.38, 2.16]
# ]
#
# name = ["NAVER", "삼성전자", "LG", "카카오"]
# title = ["종가", "PER", "PBR"]
#
# df = DataFrame(data=stock, index=name, columns=title)
# print(df)

## DataFrame 생성(3/3)
'''
2차원표에서 로우 단위로 데이터를 딕셔너리로 표현
리스트 안에 딕셔너리 표현
'''
# from pandas import DataFrame
#
# stock = [
#     {"종가": 157000, "PER": 39.88, "PBR": 4.38},
#     {"종가": 51300, "PER": 8.52, "PBR": 1.45},
#     {"종가": 68800, "PER":10.03,  "PBR": 0.87},
#     {"종가":140000, "PER": 228.38, "PBR": 2.16}
# ]
#
# name = ["NAVER", "삼성전자", "LG", "카카오"]
#
# df = DataFrame(data=stock, index=name)
# print(df)

## 연습문제
# 다음 2차원 데이터를 데이터프레임으로 생성하세요. ( 2번 로우단위로)

# from pandas import DataFrame
#
# data = [
#     [980, 990, 920, 930],
#     [200, 300, 180, 180],
#     [300, 500, 300, 400]
# ]
#
# name = ["비트코인", "리플", "이더리움"]
# column = ["시가", "고가", "저가", "종가"]
#
# df = DataFrame(data=data, index=name, columns=column)
# print(df)
# print(df.index)
# print(df.columns)
# print(df.values, type(df.values))

#### DataFrame 인덱싱과 슬라이싱 #################

## 컬럼 선택
''' 대괄호["컬럼명"] 을 통해서 단일 컬럼 선택 가능'''
# from pandas import DataFrame
#
# stock = [
#     [157000, 39.88, 4.38],
#     [51300, 8.52, 1.45],
#     [68800, 10.03, 0.87],
#     [140000, 228.38, 2.16]
# ]
#
# name = ["NAVER", "삼성전자", "LG", "카카오"]
# columns = ["종가", "PER", "PBR"]
#
# df = DataFrame(data=stock, index=name, columns=columns)
#
# print(df["종가"])     # 출력이 될때 Series 타입으로 출력이된다.
#
# 멀티 컬럼 선택
# print(df[["종가", "PBR"]])    # 여러개의 컬럼 값들을 가져올 수 있다. / df[["컬럼명1", "컬럼명2"]]   시리즈 하고 동일.

## 로우 선택

'''
데이터프레임에서 로우(row)를 선택할때는 iloc 나 loc 속성을 사용(시리즈와 동일)
iloc - 행번호 사용
loc - 인덱스 사용
'''
# from pandas import DataFrame
#
# stock = [
#     [157000, 39.88, 4.38],
#     [51300, 8.52, 1.45],
#     [68800, 10.03, 0.87],
#     [140000, 228.38, 2.16]
# ]
#
# name = ["NAVER", "삼성전자", "LG", "카카오"]
# columns = ["종가", "PER", "PBR"]
#
# df = DataFrame(data=stock, index=name, columns=columns)
#
# print(df.iloc[0])
# print(df.loc["카카오"])
#
# # 멀티 로우 선택
# print(df.iloc[[0, 2]])
# print(df.loc[["카카오", "삼성전자"]])


### 로우 슬라이싱
# from pandas import DataFrame
#
# stock = [
#     [157000, 39.88, 4.38],
#     [51300, 8.52, 1.45],
#     [68800, 10.03, 0.87],
#     [140000, 228.38, 2.16]
# ]
#
# name = ["NAVER", "삼성전자", "LG", "카카오"]
# columns = ["종가", "PER", "PBR"]
#
# df = DataFrame(data=stock, index=name, columns=columns)
#
# print(df.iloc[0:2])
# print(df.loc["NAVER" : "LG"])


#### DataFrame 값과 범위접근 ##############

## 특정 값 가져오기
'''
df.iloc[행번호, 열번호]
df.loc["인덱스", "컬럼명"]
'''
# from pandas import DataFrame
#
# data = [
#     ["3R", 1510, 7.36],
#     ["3SOFT", 1790, 1.65],
#     ["ACTS", 1185, 1.28]
# ]
#
# index = ["037730", "036360", "005760"]
# columns = ["종목명", "현재가", "등락률"]
#
# df = DataFrame(data=data, index=index, columns=columns)
#
# print(df)
# print(df.iloc[1, 1])
# print(df.loc["036360", "현재가"])

## 영역 가져오기
'''
데이터프레임에서 특정 영역 접근
df.iloc[행번호리스트, 열번호리스트]]
df.loc[인덱스리스트, 컬럼명리스트]]
'''
# from pandas import DataFrame
#
# data = [
#     ["3R", 1510, 7.36],
#     ["3SOFT", 1790, 1.65],
#     ["ACTS", 1185, 1.28]
# ]
#
# index = ["037730", "036360", "005760"]
# columns = ["종목명", "현재가", "등락률"]
#
# df = DataFrame(data=data, index=index, columns=columns)
#
# print(df)
# print(df.iloc[[0,1], [0,1]])
# print(df.loc[["037730","036360"], ["종목명", "현재가"]])

########## DataFrame 추가/ 삭제 ############################

'''
df["컬럼명"]= 시리즈 객체
비트코인 일봉 데이터를 얻어온 후 각 거래일의 변동(range) 컬럼 추가하기
    range = high - low
'''

# import pyupbit
#
# df = pyupbit.get_ohlcv(ticker="KRW-BTC")
# ## print(df)
# ## print(df.head())    # 앞에 5개(변경가능) 의 row 를 볼수있다
# ##print(df.tail())    # 뒤에 5개(변경가능) 의 row 를 볼수있다
# ## print(df["close"].tail())
#
# df["range"] = df["high"] - df["low"]        # 컬럼 추가
# print(df)

## 컬럼 삭제
'''
df.drop("컬럼명", axis=1)  1일경우 컬럼으로, 0 또는 axis를 안주면 기본적으로 행단위로
원본은 그대로 유지되고 컬럼이 삭제된 새로운 데이터프레임 객체가 리턴됨
'''
# import pyupbit
#
# df = pyupbit.get_ohlcv(ticker="KRW-BTC")
#
# df2 = df.drop("volume", axis=1)     # 원본은 그대로이므로 다른 변수에 바인딩해줌.
# print(df2)

##### 시계열 데이터와 인덱스 #######

'''
시계열 데이터는 인덱스가 날짜와 시간으로 구성됨
 - 문자열로 표현된 날짜와 시간을 DatetimeIndex 타입으로 변환해서 사용해야 함
 '''

# import pandas as pd
#
# date = ["2021-06-22"]
# index = pd.to_datetime(date)    # 이렇게 시계열데이터로 변환해서 데이터프레임생성시  index= 값에 변환된 걸 넣어준다.
#
# print(date, type(date))
# print(index, type(index))
#
# ## -----------
# date = "2021-06-22"     # 데이터가 1개일경우
# index = pd.to_datetime(date)
#
# print(date, type(date))
# print(index, type(index))


#### 로우추가
'''
loc속성을 사용
 df.loc[인덱스]= 데이터
 '''

# import pandas as pd
#
# date = "2022-01-01"
# date2 = pd.to_datetime(date)      # 우선 시계열데이터의 인덱스를 만들어줌
#
#
# import pyupbit
#
# df = pyupbit.get_ohlcv("KRW-BTC")
# print(df.tail())
#
# df.loc[date2] = [100, 100, 100, 100, 100, 100]  # 시계열데이터 추가
# print(df.tail())
# print(df.index[0])  # 데이터프레임의 처음 로우(선택가능) 를 보여줌
# print(df.loc["2021-06"])    # 6월 달에 있는 걸 다 보여준다.
#
#
# df2021_05 = df.loc["2021-05"]   # 5월달 중에
# print(df2021_05.iloc[-1])   # 제일 마지막 것만 출력

#### 로우 삭제
'''
df.drop(로우인덱스, axis=0)
 원본은 그대로 유지되고 row가 삭제된 데이터프레임 객체가 리턴됨
 '''

# import pyupbit
#
# df = pyupbit.get_ohlcv("KRW-BTC")
#
# index = df.index[-1]
# df_del = df.drop(index)
# print(df_del.tail())    # 지워진 데이터프레임 객체가 리턴됨, 원본은 그대로 유지


####### DataFrame 연산 #################

## 브로드캐스팅

import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC")

df2 = df['open'] + 100       # open 컬럼에있는 값들이 각각 모두 100씩 더해진다.


## 데이터프레임 필터링
# import pyupbit
#
# df = pyupbit.get_ohlcv("KRW-BTC")
#
# cond = df["close"] > df["open"]
# print(df[cond])     # 각 인덱스에서 True인 로우만 필터링

## 컬럼 시프트
'''
당일저가와 전일 저가를 빼려면 어떻게???
df['컬럼명'].shift(1)    -  1이면 특정컬럼을 아래로 하나씩 시프트, -1이면 위로 하나씩 시프트
'''
# import pyupbit
#
# df = pyupbit.get_ohlcv("KRW-BTC")
#
# df['종가하나내린것'] = df["close"].shift(1)
# print(df)
# a = df["close"] - df["종가하나내린것"]
# print(a)
