#python study 1
#국립환경과학원에서는 아파트에서 소음이 가장 심한 층수를 구하는 계산식을 발표했습니다. 
# 소음이 가장 심한 층은 0.2467 * 도로와의 거리(m) + 4.159입니다. 다음 소스 코드를 완성하여 소음이 가장 심한 층수가 출력되게 만드세요. 
# 단, 층수를 출력할 때는 소수점 이하 자리는 버립니다(정수로 출력).
#도로와의 거리: 12m

# distance = float(input('1. '))
# print(int(0.2467 * distance + 4.159))

###################################################################
# L이라는 게임에서 "왜곡"이라는 스킬이 AP * 0.6 + 225의 피해를 입힙니다. 참고로 이 게임에서 AP(Ability Power, 주문력)는 마법 능력치를 뜻합니다. 다음 소스 코드를 완성하여 스킬의 피해량이 출력되게 만드세요.
# AP: 102

# l_ap = float(input('2. '))
# distortion = l_ap *0.6 +225
# print(distortion)

###################################################################
#정수 세 개를 입력받고 합계가 출력되게 만드세요.

# a,b,c = map(int, input('정수 세 개를 입력하세요.').split())
# print(a+b+c)

###################################################################
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 평균 점수를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 단, 평균 점수를 출력할 때는 소수점 이하 자리는 버립니다(정수로 출력).

# korea, english, math, science = map(int, input().split())
# print((korea+english+math+science)//4)

###################################################################
#표준 입력으로 년, 월, 일, 시, 분, 초가 입력됩니다. 다음 소스 코드를 완성하여 입력된 날짜와 시간을 년-월-일T시:분:초 형식으로 출력되게 만드세요.

# year, month, day, hour, minute, second = input().split()
# print(year,month,day,sep='-',end='T')
# print(hour, minute, second, sep=':')

###################################################################
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 
# 국어는 90점 이상, 영어는 80점 초과, 수학은 85점 초과, 과학은 80점 이상일 때 합격이라고 정했습니다(한 과목이라도 조건에 만족하지 않으면 불합격). 
# 다음 소스 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되게 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
# korea, english, math, science = map(int, input().split())
# print(korea>=90 and english>80 and math>85 and science>=80)

# ###################################################################
# 표준 입력으로 정수가 입력됩니다. range의 시작하는 숫자는 -10, 끝나는 숫자는 10이며 입력된 정수만큼 증가하는 숫자가 들어가도록 튜플을 만들고, 
# 해당 튜플을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).

#리스트
# n = int(input())
# a = list(range(-10,10,n))
# print(a)

#튜플
# n = int(input())
# a = tuple(range(-10,10,n))
# print(a)

# ###################################################################
# 표준 입력으로 숫자 또는 문자열 여러 개가 입력되어 리스트 x에 저장됩니다(입력되는 숫자 또는 문자열의 개수는 정해져 있지 않음). 
# 다음 소스 코드를 완성하여 리스트 x의 마지막 요소 5개를 삭제한 뒤 튜플로 출력되게 만드세요.

# x = input().split()
# del x[-5:]
# print(tuple(x))

###################################################################

# 표준 입력으로 문자열 두 개가 각 줄에 입력됩니다(문자열의 길이는 정해져 있지 않음). 
# 첫 번째 문자열에서 인덱스가 홀수인 문자와 두 번째 문자열에서 인덱스가 짝수인 문자를 연결하여 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다). 
# 연결 순서는 첫 번째 문자열, 두 번째 문자열 순입니다. 그리고 0은 짝수로 처리합니다.

# a = input()
# b = input()
# print(a[1::2]+b[0::2])

################################################################### 

# 표준 입력으로 문자열 여러 개와 숫자(실수) 여러 개가 두 줄로 입력됩니다. 
# 입력된 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성한 뒤 딕셔너리를 출력하는 프로그램을 만드세요. 
# input().split()의 결과를 변수 한 개에 저장하면 리스트로 저장됩니다.


# name = input().split()
# value = map(float,input().split())
# lux = dict(zip(name,value))
# print(lux)

################################################################### 
# 표준 입력으로 가격(정수)과 쿠폰 이름이 각 줄에 입력됩니다. 
# Cash3000 쿠폰은 3,000원, Cash5000 쿠폰은 5,000원을 할인합니다. 
# 쿠폰에 따라 할인된 가격을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).

# cash = int(input())
# discount = input()

# if discount == 'Cash3000':
#     print(cash - 3000)
# if discount == 'Cash5000':
#      print(cash - 5000)

################################################################### 

# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 여기서 네 과목의 평균 점수가 80점 이상일 때 합격이라고 정했습니다. 
# 평균 점수에 따라 '합격', '불합격'을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 
# 단, 점수는 0점부터 100점까지만 입력받을 수 있으며 범위를 벗어났다면 '잘못된 점수'를 출력하고 합격, 불합격 여부는 출력하지 않아야 합니다.

# korea ,english , math, science= map(int, input().split())
# if 0 < korea < 101 and 0 < english < 101 and 0 < math < 101 and 0 < science < 101 :
#     if(korea+english+math+science)/4 >=80:
#         print('합격')
#     elif (korea+english+math+science)/4 <80:
#         print('불합격')
# else:
#     print('잘못된 점수')

################################################################### 

# 표준 입력으로 정수가 입력됩니다. 입력된 정수의 구구단을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 
# 출력 형식은 숫자 * 숫자 = 숫자처럼 만들고 숫자와 *, = 사이는 공백을 한 칸 띄웁니다.

# x = int(input())
# for i in range(1,10):
#     print(x,'*',i, "=", i*x)

################################################################### 

# 표준 입력으로 금액(정수)이 입력됩니다. 1회당 요금은 1,350원이고, 교통카드를 사용했을 때마다의 잔액을 각 줄에 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다). 단, 최초 금액은 출력하지 않아야 합니다. 그리고 잔액은 음수가 될 수 없으며 잔액이 부족하면 출력을 끝냅니다.

# x = int(input())
# while x >= 1350:
#     x -= 1350
#     print(x)
    
################################################################### 
# 표준 입력으로 정수 두 개가 입력됩니다
# (첫 번째 입력 값의 범위는 1~200, 두 번째 입력 값의 범위는 10~200이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 
# 다음 소스 코드를 완성하여 첫 번째 정수와 두 번째 정수 사이의 숫자 중 3으로 끝나지 않는 숫자가 출력되게 만드세요. 
# 정답에 코드를 작성할 때는 while True:에 맞춰서 들여쓰기를 해주세요.

# start, stop = map(int, input().split())
# i = start
# while True:
#     if i > stop:
#         break
#     if i%10 ==3:
#         i += 1
#         continue
#     print(i, end = ' ')
#     i += 1

################################################################### 
# 표준 입력으로 삼각형의 높이가 입력됩니다. 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 
# 이때 출력 결과는 예제와 정확히 일치해야 합니다. 모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.
# x = int(input())
# for i in range(x):
#     for j in reversed(range(x)):
#         if j > i:
#             print(end=' ')
#         if j < i: 
#             print("*",end='')
#     for jj in range(x):
#         if jj -1 < i:
#             print("*",end='')    
#     print()

################################################################### 
# for i in range(1,101):
#     if i%3 != 0 and i%5 != 0:
#         print(i)    
#     if i%3 == 0 and i%5 != 0:
#         print('Fizz')
#     if i%5 == 0 and i%3 != 0:
#         print('Buzz')
#     if i%3 == 0 and i%5 == 0:
#         print('FizzBuzz')
# ################################################################### 
# for i in range(1,101): 
#     if i%15 == 0:
#         print('FizzBuzz')
#     elif i%3 == 0:
#         print('Fizz')
#     elif i%5 == 0:
#         print('Buzz')
#     else:
#         print(i)
################################################################### 
# for i in range(1,101):
#     print('Fizz'*(i%3==0) + 'Buzz' *(i%5==0) or i)

################################################################### 
# 표준 입력으로 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 1~1000, 
# 두 번째 입력 값의 범위는 10~1000이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 
# 첫 번째 정수부터 두 번째 정수까지 숫자를 출력하면서 5의 배수일 때는 'Fizz', 7의 배수일 때는 'Buzz', 
# 5와 7의 공배수일 때는 'FizzBuzz'를 출력하는 프로그램을 만드세요

# x,y = map(int,input().split())
# for i in range(x,y+1):
#      print('Fizz'*(i%5==0) + 'Buzz' *(i%7==0) or i)

################################################################### 
#리스트 조작
# a = [10,20,30]
# b = [1,2,3]
# print(a,len(a))
# a.append(500)
# print(a,len(a))

# a.append([700,800])
# print(a,len(a))

# a.append(b)
# print(a,len(a))
# a.extend(b)
# print(a,len(a))

# a.insert(2,'w')
# print(a,len(a))

# a[1:1] = [777,888]
# print(a,len(a))

# a.pop()
# print(a,len(a))
# a.pop(2)
# print(a,len(a))

# a.remove(777)
# print(a,len(a))

# print(a.count(10))
# print(a.index(10))

# b.reverse()
# print(b,len(b))

# b.sort()
# print(b,len(b))

# a.clear()
# print(a,len(a))

################################################################### 
#리스트 할당과 조작

# a = list(range(10))
# b = a
# print('객체비교 a is b (a와 b는 같은 객체인가?)',a is b)

# b.insert(1,30)
# print('b.insert(1,30)')
# print('a : ',a,len(a))
# print('b : ',b,len(b))

# print()
# a = list(range(10,20))
# b = a.copy()
# print('객체비교 a is b (a와 b는 같은 객체인가?)',a is b)

# b.insert(1,30)
# print('b.insert(1,30)')
# print('a : ',a,len(a))
# print('b : ',b,len(b))

# print('max(a) : ',max(a),'\nmin(a) : ',min(a))
# print('sum(a) : ',sum(a))

################################################################### 
# c = [i+2 for i  in range(10)]
# print(c)

# #생성 순서
# # for i in range(10) : i 는 0부터 n-1까지의 수.
# #if i % 2 == 0 : i 중에서 2로 나눴을 때 나머지가 0인 수(짝수)
# #맨앞 i : 범위와 조건을 만족하는 i로 리스트를 만듬
# d = [i for i  in range(10) if i %2 ==0] 
# print(d)

# #순서
# #for i in range(2,11,2) : i 는 2부터 n-1 까지 2씩 커지는 수 (2,4,6,8,10)
# #j in range(1,10,2) : j 는 1부터 n-1 까지 2씩 커지는 수 (1,3,5,7,9)
# #i*j : 생성된 i 에 n번째 j를 곱함 (2 * 1, 4 * 1....) -> (2 * 3, 4 * 3....)
# e = [i * j for j in range(1,10,2) for i in range(2,11,2)]
# print(e)

################################################################### 
# a = [1.2,2.4,5.1,3.3]
# print(a)
# a = list(map(int,a))
# print('a = list(map(int,a)) : ',a)

# print('\nb = list(map(str,range(10)))')
# b = list(map(str,range(10)))
# print(b)

#이는 데이터를 추가,수정,삭제하는 것 이외에는 튜플도 가능하다

###################################################################
# 표준 입력으로 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 1~20, 두 번째 입력 값의 범위는 10~30이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다).
# 첫 번째 정수부터 두 번째 정수까지를 지수로 하는 2의 거듭제곱 리스트를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 
# 단, 리스트의 두 번째 요소와 뒤에서 두 번째 요소는 삭제한 뒤 출력하세요. 출력 결과는 리스트 형태라야 합니다.
# x,y = map(int,input().split())
# a = [2 ** i for i in range(x,y+1)]
# a.pop(1)
# a.pop(-2)
# print (a)

###################################################################
# a = [[i+j for i in range(2)]for j in range(4)]
# print(a)

# b = [[i]*2 for i in range(4)]
# print(b)

# c =[]
# for i in range(4):
#     line = []
#     for j in range(2):
#         line.append(i+j)
#     c.append(line)
# print (c)

###################################################################

# #톱니형 리스트

# d = [3,1,2,5] # 가로 크기를 저장한 리스트
# e = []

# for i in d: #리스트의 가로 크기
#     in_list = []
#     for j in range(i):
#         in_list.append(i) #i만큼 안쪽 리스트에 i를 추가
#     e.append(in_list)       #리스트 e에 만들어진 안쪽 리스트 추가
# print (e)

###################################################################
# #2차 리스트 정렬

# students = [
#     ['john', 'C', 19],
#     ['maria', 'A', 25],
#     ['andrew', 'B', 20]
# ]
# #sorted(반복 가능한 객체, key = 정렬 함수 , reverse = True or False)
# print(sorted(students, key=lambda student: student[0])) #리스트를 안쪽 리스트의 첫 번째 요소를 기준으로 정렬
# print(sorted(students, key=lambda student: student[1])) #리스트를 안쪽 리스트의 두 번째 요소를 기준으로 정렬
# print(sorted(students, key=lambda student: student[2])) #리스트를 안쪽 리스트의 세 번째 요소를 기준으로 정렬

###################################################################
#2차 리스트의 할당과 복사

# a = [[1,2],[3,4],[5,6]]
# b = a
# print(a,b,sep='\n')

# b [0][0] = 7
# print(a,b,sep='\n')

# print()
# c = [[1,2],[3,4],[5,6]]
# d = c.copy()
# print(c,d,sep='\n')

# c[0][0] = 8
# print(c,d,sep='\n')

# print()
# import copy
# e = [[1,2],[3,4],[5,6]]
# f = copy.deepcopy(e)
# print(e,f,sep='\n')

# e[0][0] = 9
# print(e,f,sep='\n')

###################################################################
# 표준 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고 그 다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다. 
# 이때 2차원 리스트 안에서 *는 지뢰이고 .은 지뢰가 아닙니다. 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는 프로그램을 만드세요.
#입력
# 3 3
# .**
# *..
# .*.

# #결과
# 2**
# *43
# 2*1

# col,row = map(int,input().split())
# matrix = []
# for i in range(row):
#     matrix.append(list(input()))

# for i in range(col):
#     for j in range(row):
#         if matrix[i][j] != '*':
#             matrix[i][j] = 0
#             for x in range(i-1, i+2):
#                 for y in range(j -1, j +2):
#                     if y < 0 or x < 0 or y >= row or x >= col:
#                         continue
#                     if matrix[x][y] == '*':
#                         matrix[i][j] +=1
#             print(matrix[i][j],end='')
#         else:
#             print(matrix[i][j],end='')
#     print()

# for i in matrix:
#     print()
#     for j in i:
#         print(j,end='')

###################################################################
#문자열 조작
# a = 'Hello, world!'
# b = a.replace('world','Python')
# print(a,b,sep='\n')

# print()
# print('apple')
# table = str.maketrans('aeiou','12345')
# print("table = str.maketrans('aeiou','12345')",end='\n')
# print("apple'.translate(table) : ",'apple'.translate(table))

# print()
# c = 'apple pear grape pineapple orange'
# print(c)
# d = c.split()
# print('c.split() : ',d)

# print()
# print('d : ',d)
# print("'-'.join(d) : ",'-'.join(d))

# print()
# print("'python'.upper() : ",'python'.upper())
# print("'PYTHON'.lower() : ",'PYTHON'.lower())

# print()
# print("'   Python   '.lstrip() : ",'   Python   '.lstrip())
# print("'   Python   '.rstrip() : ",'   Python   '.rstrip())
# print("'   Python   '.strip() : ",'   Python   '.strip())
# print("', python.'.strip(',.') : ",', python.'.strip(',.'))

# print()
# print("'python'.center(10) : ",'python'.center(10))
# print('python'.rjust(10))
# print('python'.ljust(10))

# print()
# print("'python'.rjust(10).upper() : ",'python'.rjust(10).upper())

# print()
# print("'apple pineapple'.find('pl') : ", 'apple pineapple'.find('pl'))
# print("'apple pineapple'.rfind('pl') : ", 'apple pineapple'.rfind('pl'))
# print("'apple pineapple'.index('pl') : ",'apple pineapple'.index('pl'))
# print("'apple pineapple'.rindex('pl') : ",'apple pineapple'.rindex('pl'))

# print()
# print("'apple pineapple'.count('pl') : ",'apple pineapple'.count('pl'))

# print()
# print("'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6) : ",'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6))
# print("'Hello, {language} {version}'.format(language='Python', version=3.6) : ", 'Hello, {language} {version}'.format(language='Python', version=3.6)
# )

###################################################################
#표준 입력으로 문자열이 입력됩니다. 입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 
# 단, 모든 문자가 소문자인 'the'만 찾으면 되며 'them', 'there', 'their' 등은 포함하지 않아야 합니다.

# x = input()
# xcount = 0
# x = x.split()
# for i in x:
#     if i.strip(',.') == 'the':
#         xcount +=1
# print(xcount)

###################################################################
# 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다. 
# 입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 
# 이때 가격은 길이를 9로 만든 뒤 오른쪽으로 정렬하고 천단위로 ,(콤마)를 넣으세요.

# price = list(map(int,input().split(';')))
# price.sort(reverse=True)
# for i in price:
#     print('{0: >9,}'.format(i,','))

###################################################################
#딕셔너리 조작

# x = {'a' : 10, 'b' : 20, 'c' : 30}
# print(x)
# print("x.setdefault('d')")
# x.setdefault('d')
# print(x)
# print("x.setdefault('e',100)")
# x.setdefault('e',100)
# print(x)

# print()
# print("x.update(a=200)")
# x.update(a=200)
# print(x)
# print("x.update(f=3000)")
# x.update(f=3000)
# print(x)

# print()
# print("x.update({1:'ONE'})")
# x.update({1:'ONE'})
# print(x)
# print("x.update([[2, 'TWO'], [4, 'FOUR']])")
# x.update([[2, 'TWO'], [4, 'FOUR']])
# print(x)
# print("x.update(zip([1, 2], ['one', 'two']))")
# x.update(zip([1, 2], ['one', 'two']))
# print(x)

# print()
# print("x.pop('a')")
# x.pop('a')
# print(x)

# print("del x['d']")
# del x['d']
# print(x)

# print()
# print("y = x.copy()")
# y = x.copy()
# print(y)
# print("y.clear()")
# y.clear()
# print(y,sep='\n')

# print()
# print("x.get('b') : ",x.get('b'))
# print("x.items() : ",x.items())
# print("x.keys() : ",x.keys())
# print("x.values() : ",x.values())

# print()
# keys = ['a', 'b', 'c']
# print("keys : ",keys)
# z = dict.fromkeys(keys,100)
# print("z = dict.fromkeys(keys,100) : ",z)

# print()
# from collections import defaultdict
# print("from collections import defaultdict")
# i = defaultdict(int)
# print("i = defaultdict(int)")
# print("i['y'] : ", i['y'])

# print()
# for key, value in x.items():
#     print(key, value)

# print()
# for key in x.keys():
#     print(key)

# print()
# for value in x.values():
#     print(value)

# print()
# print("{value: key for key, value in x.items()}\n",{value: key for key, value in x.items()})
# print()
# print("x = {key: value for key, value in x.items() if value != 'FOUR'}")
# x = {key: value for key, value in x.items() if value != 'FOUR'}
# print(x)

# print()
# terrestrial_planet = {
#     'Mercury': {
#         'mean_radius': 2439.7,
#         'mass': 3.3022E+23,
#         'orbital_period': 87.969
#     },
#     'Venus': {
#         'mean_radius': 6051.8,
#         'mass': 4.8676E+24,
#         'orbital_period': 224.70069,
#     },
#     'Earth': {
#         'mean_radius': 6371.0,
#         'mass': 5.97219E+24,
#         'orbital_period': 365.25641,
#     },
#     'Mars': {
#         'mean_radius': 3389.5,
#         'mass': 6.4185E+23,
#         'orbital_period': 686.9600,
#     }
# }
# print(terrestrial_planet['Venus']['mean_radius'])

###################################################################
# 표준 입력으로 문자열 여러 개와 숫자 여러 개가 두 줄로 입력되고, 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성합니다. 
# 다음 코드를 완성하여 딕셔너리에서 키가 'delta'인 키-값 쌍과 값이 30인 키-값 쌍을 삭제하도록 만드세요.

# keys = input().split()
# values = map(int,input().split())
# x = dict(zip(keys,values))
# x = {key: value for key, value in x.items() if key != 'delta'}
# x = {key: value for key, value in x.items() if value != 30}
# print(x)

###################################################################
#세트 조작

# apple = set('apple')
# pineapple = set('pineapple')
# blueberry = set('blueberry')
# print(apple,pineapple,sep = '\n' )

# print()
# print("'a' in apple : ", 'a' in apple)
# print("'c' in apple : ", 'c' in apple)

# print()
# c = blueberry|pineapple
# print("c = blueberry|pineapple : ",c)
# c = blueberry&pineapple
# print("c = blueberry&pineapple : ",c)
# c = pineapple-apple
# print("c = pineapple-apple : ",c)
# c = apple^pineapple
# print("c = apple^pineapple : ",c)

# print()
# apple = set('apple')
# apple.update('c')
# print("apple.update('c') : ",apple)
# apple |= {'s'}
# print("apple |= {'s'} : ", apple)

# print()
# apple = set('apple')
# apple.intersection_update(pineapple)
# print('apple.intersection_update(pineapple) : ',apple)
# apple &= blueberry
# print('apple &= blueberry : ', apple)

# print()
# apple = set('apple')
# apple.difference('a')
# print("apple.difference('a') : ", apple)
# apple -= {'p'}
# print("apple -= {'p'} : ", apple)

# print()
# apple = set('apple')
# apple.symmetric_difference_update(blueberry)
# print("apple.symmetric_difference_update(blueberry) : ",apple)
# apple ^= pineapple
# print("apple ^= pineapple : ",apple)

# print()
# apple = set('apple')
# print("apple <= pineapple : ",apple <= pineapple)
# print("apple.issubset(pineapple) : ",apple.issubset(pineapple))

# print()
# apple = set('apple')
# print("apple >= pineapple : ",apple >= pineapple)
# print("pineapple.issubset(apple) : ",pineapple.issubset(apple))

# print()
# print("apple < pineapple : ",apple < pineapple)

# print()
# print("apple > pineapple : ",apple > pineapple)

# print()
# a = set('apple')
# print("apple == a : ",apple == a)
# print("apple == pineapple : ", apple != pineapple)
# print("(apple.isdisjoint(a) : ",apple.isdisjoint(a))
# print("(apple.isdisjoint({'cheese'}) : ",apple.isdisjoint({'cheese'}))

###################################################################
# a = set(range(5))
# print(a)
# a.add(5)
# print("a.add(5) : ",a)

# a.remove(3)
# print("a.remove(3) : ",a)
# #a.remove(3) #error

# a.discard(2)
# print("a.discard(2) : ",a)
# a.discard(2) #not in value -> pass
# print("a.discard(2) : ",a)

# a.pop()
# print("a.pop() : ",a)

# a.clear()
# print("a.clear() : ",a)

# a = set(range(5))
# print("len(a) : ",len(a))

###################################################################
# a = set(range(5))
# for i in a:
#     print(i,end=' ')

# print()
# b = {i for i in 'pineapple'}
# print(b)


# c = {i for i in 'pineapple' if i not in 'apple'}
# print(c)

###################################################################
# 표준 입력으로 양의 정수 두 개가 입력됩니다. 다음 소스 코드를 완성하여 두 숫자의 공약수를 세트 형태로 구하도록 만드세요. 
# 단, 최종 결과는 공약수의 합으로 판단합니다
# num1, num2 = map(int, input().split())
# a = {i for i in range(1,num1+1) if (num1 % i) == 0}
# b = {i for i in range(1,num2+1) if (num2 % i) == 0}
# divisor = a&b
# result = 0
# if type(divisor) == set:
#     result = sum(divisor)
# print(result)

###################################################################
# file = open('hello world.txt', 'w')
# file.write('파이썬 파일 관리 한글 테스트')
# file.close()

# file = open('hello world.txt', 'r')
# s = file.read()
# print(s)
# file.close()

# with open('hello world.txt','r') as file:
#     s = file.read()
#     print(s)

# lines = ['파이썬 파일 읽기 쓰기\n', '한글 입력 테스트']
# with open ('hello world.txt','w') as file:
#     file.writelines(lines)

# with open ('hello world.txt', 'r') as file:
#     lines2 = file.readlines()
#     print(lines2)

# with open ('hello world.txt', 'r') as file:
#     lines3 = None
#     while lines3 != '':
#         lines3 = file.readline()
#         print(lines3.strip('\n'))

# with open('hello.txt', 'w') as file:
#     for i in range(3):
#         file.write("파이썬 파일관리 한글 테스트 {0}\n".format(i))

###################################################################
# import pickle

# name = 'james'
# age = 17
# address = '경기도 남양주시 와부읍'
# scores = {'korean': 90, 'english': 70, 'math': 60, 'science': 80}

# with open('james.p','wb') as file:
#     pickle.dump(name,file)
#     pickle.dump(age,file)
#     pickle.dump(address,file)
#     pickle.dump(scores,file)

# with open('james.p','rb') as file:
#     o_name  = pickle.load(file)
#     o_age = pickle.load(file)
#     o_address = pickle.load(file)
#     o_scores = pickle.load(file)

#     print(o_name,o_age,o_address,o_scores,sep='\n')

###################################################################
# 27.5 연습문제: 파일에서 10자 이하인 단어 개수 세기
# 단어가 줄 단위로 저장된 words.txt 파일이 주어집니다. 다음 소스 코드를 완성하여 10자 이하인 단어의 개수가 출력되게 만드세요

# with open('words1.txt','r') as file:
#     words_list = file.readlines()
# print(words_list)
# count = 0
# for word in words_list:
#     if len(word.strip('\n')) <= 10:
#         count +=1
# print(count)


###################################################################

# 문자열이 저장된 words.txt 파일이 주어집니다(문자열은 한 줄로 저장되어 있습니다). 
# words.txt 파일에서 문자 c가 포함된 단어를 각 줄에 출력하는 프로그램을 만드세요. 
# 단어를 출력할 때는 등장한 순서대로 출력해야 하며 ,(콤마)와 .(점)은 출력하지 않아야 합니다.

# with open('words2.txt','r') as file:
#     words_list = file.readlines()
# words_list_split = str(words_list).split()

# for word in words_list_split:
#     if 'c' in word:
#         print(word.strip(',.'))

###################################################################
#회문 판결

# word = input('단어를 입력하세요: ')
 
# is_palindrome = True                 # 회문 판별값을 저장할 변수, 초깃값은 True
# for i in range(len(word) // 2):      # 0부터 문자열 길이의 절반만큼 반복
#     if word[i] != word[-1 - i]:      # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
#         is_palindrome = False        # 회문이 아님
#         break
 
# print(is_palindrome)                 # 회문 판별값 출력



# word = input("단어를 입력하세요.\n")
# print(word == word[::-1])

# word = input("단어를 입력하세요.\n")
# print(list(word) == list(reversed(word)))

# word = input("단어를 입력하세요.\n")
# print(word == "".join(reversed(word)))

###################################################################
#n-gram

# text = "Python"
# for i in range(len(text)-1):
#     print(text[i],text[i+1],sep='')

# text = "Python"
# for i in range(len(text)-2):
#     print(text[i],text[i+1],text[i+2],sep='')

# text = 'this is python script'
# words = text.split()                 # 공백을 기준으로 문자열을 분리하여 리스트로 만듦
 
# for i in range(len(words) - 1):      # 2-gram이므로 리스트의 마지막에서 요소 한 개 앞까지만 반복함
#     print(words[i], words[i + 1])    # 현재 문자열과 그다음 문자열 출력


# text = "Python"
# two_gram = zip(text,text[1:])
# for i in two_gram:
#     print(i[0],i[1],sep='')

# text = "Python"
# two_gram = list(zip(text,text[1:],text[2:]))
# for i in two_gram:
#     print(i[0],i[1],i[2],sep='')

# text = 'this is python script'
# words = text.split()
# two_gram = list(zip(words, words[1:]))
# print(two_gram)

# text = "Python"
# three_gram = list(zip(*[text[i:] for i in range(3)]))
# print(three_gram)


###################################################################

# 연습문제: 단어 단위 N-gram 만들기
# 표준 입력으로 정수와 문자열이 각 줄에 입력됩니다. 
# 다음 소스 코드를 완성하여 입력된 숫자에 해당하는 단어 단위 N-gram을 튜플로 출력하세요(리스트 표현식 사용). 
# 만약 입력된 문자열의 단어 개수가 입력된 정수 미만이라면 'wrong'을 출력하세요.


# from sys import stdin
# n = int(stdin.readline())
# text = stdin.readline()
# words = text.split()

# if len(words) < n:
#     print('wrong')
# else:
#     n_gram = list(zip(*[words[i:] for i in range(n)]))
#     for i in n_gram:
#         print(i)

###################################################################

# 단어가 줄 단위로 저장된 words.txt 파일이 주어집니다.
# words.txt 파일에서 회문인 단어를 각 줄에 출력하는 프로그램을 만드세요. 
# 단어를 출력할 때는 등장한 순서대로 출력해야 합니다. 
# 그리고 파일에서 읽은 단어는 \n이 붙어있으므로 \n을 제외한 뒤 회문인지 판단해야 하며 단어를 출력할 때도 \n이 출력되면 안됩니다.
# (단어 사이에 줄바꿈이 두 번 일어나면 안 됨).

# with open('words3.txt','r') as file:
#     word_list = file.readlines()
# for word in word_list:
#     s_word = word.strip('\n')
#     if s_word == ''.join(reversed(s_word)):
#         print(s_word)


###################################################################

# 파일 열기, 닫기

# 파일 읽기/쓰기를 하기 전에는 open 함수로 파일을 열어서 파일 객체를 얻어야 합니다. 
# 그다음에 파일 읽기/쓰기 작업이 끝났다면 반드시 close로 파일 객체를 닫아줍니다.

# 파일객체 = open(파일이름, 파일모드)    # 파일 열기
# 파일객체.close()                       # 파일 객체 닫기
 
# with open(파일이름, 파일모드) as 파일객체:    # 파일을 사용한 뒤 자동으로 파일 객체를 닫아줌
#     코드

###################################################################

# 파일 모드

# 'r'

# 읽기 전용
# 파일을 읽기 전용으로 열기. 단, 파일이 반드시 있어야 하며 파일이 없으면 에러 발생

# 'w'

# 쓰기 전용
# 쓰기 전용으로 새 파일을 생성. 만약 파일이 있으면 내용을 덮어씀

# 'a'

# 추가
# 파일을 열어 파일 끝에 값을 이어 씀. 만약 파일이 없으면 파일을 생성

# 'x'

# 배타적 생성(쓰기)
# 파일을 쓰기 모드로 생성. 파일이 이미 있으면 에러 발생

# 'r+'

# 읽기/쓰기
# 파일을 읽기/쓰기용으로 열기. 단, 파일이 반드시 있어야 하며 파일이 없으면 에러 발생

# 'w+'

# 읽기/쓰기
# 파일을 읽기/쓰기용으로 열기. 파일이 없으면 파일을 생성하고, 파일이 있으면 내용을 덮어씀

# 'a+'

# 추가(읽기/쓰기)
# 파일을 열어 파일 끝에 값을 이어 씀. 만약 파일이 없으면 파일을 생성. 
# 읽기는 파일의 모든 구간에서 가능하지만, 쓰기는 파일의 끝에서만 가능함

# 'x+'

# 배타적 생성(읽기/쓰기)
# 파일을 읽기/쓰기 모드로 생성. 파일이 이미 있으면 에러 발생

# t

# 텍스트 모드
# 파일을 읽거나 쓸 때 개행 문자 \n과 \r\n을 서로 변환
# t를 생략하면 텍스트 모드

# b

# 바이너리 모드
# 파일의 내용을 그대로 읽고, 값을 그대로 씀

###################################################################

# 파일 메서드

# read()
# 파일에서 문자열을 읽음

# write('문자열')
# 파일에 문자열을 씀

# readline()
# 파일의 내용을 한 줄 읽음

# readlines()
# 파일의 내용을 한 줄씩 리스트 형태로 가져옴

# writelines(문자열리스트)
# 파일에 리스트의 문자열을 씀, 리스트의 각 문자열에는 \n을 붙여주어야 함

# pickle.load(파일객체)
# 파일에서 파이썬 객체를 읽음

# pickle.dump(객체, 파일객체)
# 파이썬 객체를 파일에 저장


###################################################################

# 표준 입력으로 숫자 두 개가 입력됩니다. 
# 다음 소스 코드를 완성하여 두 숫자의 덧셈, 뺄셈, 곱셈, 나눗셈의 결과가 출력되게 만드세요. 
# 이때 나눗셈의 결과는 실수라야 합니다.

# x, y = map(int, input().split())

# def calc(a, b):
#     return a+b, a-b, a*b, a/b

# a,s,m,d = calc(x,y)
# print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a,s,m,d))

###################################################################

#위치 인수와 언패킹

# def print_numbers(a,b,c):
#     print(a)
#     print(b)
#     print(c)

# x = [10,20,30]
# print_numbers(*x)



# def print_args(*args):
#     for arg in args:
#         print(arg)
# n = int(input())
# y = [(_ + 1) * 10 for _ in range(n)]
# print_args(*y)

# 참고 | 고정 인수와 가변 인수를 함께 사용하기
# 고정 인수와 가변 인수를 함께 사용할 때는 다음과 같이 고정 매개변수를 먼저 지정하고, 그 다음 매개변수에 *를 붙여주면 됩니다.

# def print_num_args(a, *args):
#      print(a)
#      print(args)

# print_num_args(1)

# print_num_args(1, 10, 20)

# print_num_args(*[10, 20, 30])

# 단, 이때 def print_num_args(*args, a):처럼 *args가 고정 매개변수보다 앞쪽에 오면 안 됩니다. 
# 매개변수 순서에서 *args는 반드시 가장 뒤쪽에 와야 합니다.



###################################################################
#키워드 인수 사용


# def personal_info(name, age, address):
#      print('이름: ', name)
#      print('이름: ', name)
#      print('나이: ', age)
#      print('주소: ', address)

# personal_info(age=25, name='허성민', address='경기도 남양주시 와부읍')