# 요일을 저장할 수 있는 리스트 ls를 생성하고 출력하세요

# ls = ['월', '화', '수', '목', '금', '토', '일']

# print(ls[1])


# ls에서 현재 요일에 해당하는 값만 출력하세요 
# print(ls[5])


# # 토, 일요일만 저장하는 리스트 we를 생성하세요.
# # 이때, 리스트 호기화는 ls를 이용하세요

# we = ls[5:7]
# print(we)

# ls에서 토,일 값을 삭제해라

# del ls[5:7]
# del ls[1]
# print(ls)

# 리스트 days를 생성하여 ls와 we값을 전부 할당하세요.

# days = ls+we
# print(days)

# # days의 요소들을 역순으로 뒤집어서 출력하세요

# days.reverse()
# print(days)

# # 리스트 복제

# daysr = days.copy()
# daysr.reverse()
# print(daysr)

# days 요소들을 가나다 순으로 정렬하세요.
# days.sort()

# index함수로 수요일이 몇번째 위치에 있는지 알아내세요.
# del함수로 수요일을 제거하세요.

# print(days.index('수'))

# print(ls[2])

# del days[days.index('수')]
# print(days)

# days.remove('금')
# print(days)

# 리스트와 튜플의 차이점
# 리스트는 대괄호 튜플은 소괄호 리스트는 수정이 가능하지만 튜플은 고정적인 값이다.

# 이름 국어 영어 수학 점수를 저장하는 리스트를 생성하세요.

ls = {'name':'김지태', 'kor':100, 'eng':50, 'math':53}

# 딕셔너리의 키 값만 추출하여 출력하세요.
# 각 각 요소의 데이터에 이름을 지저아혹, 영어점수를 출력하세요

print(ls['eng'])
print(ls.keys())

tmp = ls.values() #keys, values
print(tmp)