import itertools


def spam(left, right):
    return left * right

# itertools.accumulate : iterable 객체의 모든 요소를 계산한다. 두번째 파라미터를 생략하면 operator.add()가 기본이며, 함수를 지정하면
# 지정한 함수의 계산을 수행한다.
for v in itertools.accumulate([1, 2, 3], spam):
    print(v)

it = itertools.accumulate([1, 2, 3, 4], spam)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print('=' * 20)

# itertools.chain : iterable 객체 여러 개를 연결한 iterator를 만든다.
it2 = itertools.chain([1, 2, 3], {'a', 'b', 'c'})
for v in it2:
    print(v)
print('=' * 20)

iters = ([1, 2, 3], {'a', 'b', 'c'})
for c in itertools.chain.from_iterable(iters):
    print(c)
print('=' * 20)

# itertools.permutations : 순열 구하기
for v in itertools.permutations('ABC', 2):
    print(v)
print('=' * 20)

# itertools.combinations : 조합 구하기
for v in itertools.combinations('ABC', 2):
    print(v)
print('=' * 20)

# itertools.combinations_with_replacement : 중복을 포함한 조합 구하기
for v in itertools.combinations_with_replacement('ABC', 2):
    print(v)
print('=' * 20)

# itertools.product : 직적(direct product) 구하기
for v in itertools.product('ABC', [1, 2, 3]):
    print(v)
