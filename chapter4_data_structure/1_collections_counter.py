import collections

# Counter 객체를 통해 딕셔너리에 있는 데이터의 건수를 카운트할 수 있음.
c = collections.Counter()
c['spam'] += 1
c[100] += 1
c[200] += 1
c[200] += 3
print(c)

counter1 = collections.Counter([1, 2, 3, 1, 2, 1, 2, 1])
print(counter1)

# 등록되어 있는 않은 키 값을 참조하면 0이 반환됨. 예외 발생하지 않음.
counter2 = collections.Counter()
print(counter2['spam'])

counter2['spam'] += 1
print(counter2)

counter3 = collections.Counter(spam=1, ham=2)
counter4 = collections.Counter(ham=3, egg=4)
print(counter3 + counter4)
print(counter3 - counter4)
print(counter3 & counter4)
print(counter3 | counter4)

counter3 += counter4
print(counter3)

counter5 = collections.Counter(spam=-1, ham=2)
counter6 = collections.Counter(ham=2, egg=-3)
print(counter5 + counter6)
print(counter5 - counter6)

counter7 = collections.Counter(spam=-1, ham=2)
print(+counter7)
print(-counter7)
