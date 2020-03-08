# 입력값이 60 이상이면 합격이라고 출력하세요.


# val = eval(input('점수를 입력해주세요 : '))
# if val >= 60:
#     print('합격')
# else:
#     print('불합격') 


# elif를 이용하여 90이상이면 합격, 80이상이면 재시험
# 그 이외에는 불합격이라고 출력하세요.

# if val >= 90:
#     print('합격')
# elif val >=80:
#     print('재시험')
# else:
#     print('불합격') 

# 두 과목 점수의 평균이 60이상이면서
# 각각 40이상이면 합격이라고 출력하세요.
# s1 = eval(input('입렭 : '))
# s2 = eval(input('입력 : '))

# avg = (s1 + s2) / 2
# if avg >= 60 and s1>=40 and s2 >= 40:
#     print('합격')
# else:
#     print('불합겨')

# 3개의 정수 중 가장 큰 값을 출력하세요.
# s1 = eval(input('입렭 : '))
# s2 = eval(input('입력 : '))
# s3 = eval(input('입력 : '))

# if s1 > s2:
#     if s1 > s3:
#         print('s1이 가장 큽니다.')
#     else:
#         print('s3 is big')
# else:
#     if s2 > s3:
#         print('s2 is big')
#     else:
#         print('s3 is big')

# ls = []

# s3 = eval(input('입력 : '))
# ls.append(s3)
# s3 = eval(input('입력 : '))
# ls.append(s3)
# s3 = eval(input('입력 : '))
# ls.append(s3)
# ls.sort()
# ls.reverse()
# print(ls[0])

# 연도를 입력받아서 윤년이지 평년인지 판단하여 출력하세요
# 400의 약수, 4의 배수중 100의 배수가 아닌 수 
# s = int(input('입력 : '))
# if s % 400 == 0 or (s % 4 == 0 and s % 100 != 0):

# 리스트를 활용하여 입력받은 월의 날수를 출력하세요
# 31 28 31 30 31 30 31 31 30 31 30 31

s = int(input('월을 입력하세요 : '))

# ls = [31, 28, 31, 30 ,31 ,30, 31, 31, 30, 31, 30, 31]
# print(ls[s-1])

a = [1, 3, 5, 7, 8, 10, 12]
if s in a:
    print('31')
elif s == 2:
    print(28)
else:
    print('30')
