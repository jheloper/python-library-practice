import collections

c = collections.Counter()
c['spam'] += 1
c[100] += 1
c[200] += 1
c[200] += 3
print(c)

counter1 = collections.Counter([1, 2, 3, 1, 2, 1, 2, 1])
print(counter1)

countet2 = collections.Counter()
print(countet2['spam'])

countet2['spam'] += 1
print(countet2)

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
