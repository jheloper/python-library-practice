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

# 정규식 객체를 반환.
regex = re.compile('[a-n]+')

print(type(regex))

print(regex.search('python'))

print(regex.match('python'))

# 지정 문자열 전체가 정규식에 일치하는지 확인.
print(regex.fullmatch('eggs'))

print(regex.fullmatch('egg'))

regex2 = re.compile('[-+()]')

print(regex2.split('012-3456-7890'))

print(regex2.split('(012)3456-7890'))

print(regex2.split('+81-80-3456-7890'))

# 문자열 안의 정규식에 일치한 문자열을 1번째 파라미터로 치환.
print(regex2.sub('', '+81-80-3456-7890'))

regex3 = re.compile('\d+')

print(regex3.findall('012-3456-7890'))

for m in regex3.finditer('+81-80-3456-7890'):
    print(m)
