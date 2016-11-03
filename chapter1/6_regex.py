import re

# 지정된 문자열의 정규식 일치 여부 확인. 문자열의 맨 앞글자부터 일치하는지 확인.
print(re.match('a.c', 'abc'))

# 지정된 문자열의 정규식 일치 여부 확인.
print(re.search('a.c', 'abc'))

print(re.match('b', 'abc'))

print(re.search('b', 'abc'))

print(re.search('\w', '가나다라마ABC'))

# re.A는 아스키 문자 상수 플래그.
print(re.search('\w', '가나다라마ABC', flags=re.A))

print(re.search('[abc]+', 'ABC'))

# re.I는 대소문자 무시 플래그.
print(re.search('[abc]+', 'ABC', re.I))

print(re.match('a.c', 'A\nC', re.I))

# |을 통해 여러 개의 플래그 지정 가능. re.S는 Dot(.)을 줄바꿈까지 포함 플래그.
print(re.match('a.c', 'A\nC', re.I | re.S))
