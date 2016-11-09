import collections

d1 = {'spam': 1}
d2 = {'ham': 2}

# ChainMap으로 여러 딕셔너리를 모아서 하나의 딕셔너리로 만들기.
c = collections.ChainMap(d1, d2)
print(c['spam'], c['ham'])

# ChainMap 객체의 요소를 추가 or 삭제하면, 첫번째 파라미터인 매핑 객체에 반영됨.
c['bacon'] = 3
print(d1)

c.clear()
print(d1)

# KeyError: 'ham'
d3 = {'spam': 100}
# print(d3['ham'])

print(d3['spam'])


def value():
    return 'default-value'

# defaultdict를 통해 기본값이 존재하는 딕셔너리 생성 가능. 등록되어 있지 않은 키를 참조해도 예외 발생하지 않고 기본값으로 반환.
d4 = collections.defaultdict(value, spam=100)
print(d4)
print(d4['ham'])

# 파라미터로 int를 지정하면 기본값이 정수 0으로 설정.
d5 = collections.defaultdict(int)
print(d5['spam'])

d5['spam'] += 100
print(d5)

# 파라미터로 list를 지정하면 기본값이 비어있는 리스트.
d6 = collections.defaultdict(list)
d6['spam'].append(100)
d6['spam'].append(200)
print(d6)
