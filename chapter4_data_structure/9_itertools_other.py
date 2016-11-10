import itertools
import random


def is_even(n):
    return n % 2 == 0

# filter : 내장 함수. iterable 객체에서 특정 조건을 만족하는 값만 추출.
for v in filter(is_even, [1, 2, 3, 4, 5, 6]):
    print(v)
print('=' * 20)

# filter 첫번째 파라미터에 None을 지정하면 True인 값만 반환함.
items = [1, 0, 'Spam', '', [], [1]]
for v in filter(None, items):
    print(v)
print('=' * 20)

# itertools.filterfalse : 특정 조건이 False인 값만 반환.
for v in itertools.filterfalse(is_even, [1, 2, 3, 4, 5, 6]):
    print(v)
print('=' * 20)

for v in itertools.filterfalse(None, items):
    print(v)
print('=' * 20)

# itertools.compress : 두번째 파라미터에서 얻은 값이 True이면 첫번째 파라미터에서 해당 값과 쌍을 이루는 값을 반환.
for v in itertools.compress(['spam', 'ham', 'egg'], [1, 0, 1]):
    print(v)
print('=' * 20)

# itertools.count : 두 값의 등차수열을 만듬.
for v in itertools.count(1, 2):
    if v > 5:
        break
    print(v)

# itertools.islice : iterable 객체에서 지정한 범위의 값을 얻음.
print(list(itertools.islice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5)))

print(list(itertools.islice(itertools.count(1, 1), 3, 8, 2)))


def is_odd(n):
    return n % 2

# itertools.dropwhile : 지정한 함수의 조건을 만족하는 동안은 drop, 그 후에는 모든 값을 반환.
print(list(itertools.dropwhile(is_odd, [1, 1, 1, 2, 3, 4])))

# itertools.takewhile : 지정한 함수의 조건을 만족하는 동안에만 값을 반환함.
print(list(itertools.takewhile(is_odd, [1, 1, 1, 2, 3, 4])))

print(list(itertools.repeat('a', 5)))
print('=' * 20)

# itertools.cycle : 지정한 iterable 객체의 모든 값을 반복.
for c in itertools.islice(itertools.cycle('abc'), 1, 5):
    print(c)
print('=' * 20)

for value, group in itertools.groupby(['a', 'b', 'b', 'c', 'c', 'c']):
    print(value, group, tuple(group))
print('=' * 20)

for value, group in itertools.groupby([10, 20, 31, 11, 3, 4], is_odd):
    print(value, group, tuple(group))
print('=' * 20)

# zip : 내장 함수. 지정한 여러 개의 iterable 객체로부터 값을 하나씩 얻어 이를 튜플로 반환.
for v in zip((1, 2, 3), ('a', 'b', 'c'), ('가', '나', '다')):
    print(v)

matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
transformed = list(zip(*matrix))
print(transformed)
print('=' * 20)

# itertools.zip_longest : zip과는 달리 모든 iterable 객체의 모든 값으로부터 튜플을 생성함. fillvalue 파라미터 지정.
for v in itertools.zip_longest('abcdefg', '123', '가나다라마', fillvalue='-'):
    print(v)
print('=' * 20)

# map : 내장 함수. iterable 객체의 값에 함수를 적용하여 다른 값으로 변환함.
for v in map(chr, [0x40, 0x41, 0x42, 0x43]):
    print(v)
print('=' * 20)

for v in map(min, 'spam', 'ham', 'egg'):
    print(v)
print('=' * 20)

# itertools.starmap : 파라미터를 iterable 객체에 저장하여 지정하는 점을 빼면 map과 동일.
iterables = ['spam', 'ham', 'egg']
for v in itertools.starmap(min, iterables):
    print(v)
print('=' * 20)

# 위의 itertools.starmap(min, iterables)과 아래 map(min, *iterables)은 같음.
for v in map(min, *iterables):
    print(v)
print('=' * 20)


def values():
    for i in range(10):
        yield random.random()

it = values()

# itertools.tee : iterable 복제. 두번째 파라미터로 복제할 갯수를 지정한다.
a, b, c = itertools.tee(it, 3)
print(sum(a), sum(b), sum(c))
