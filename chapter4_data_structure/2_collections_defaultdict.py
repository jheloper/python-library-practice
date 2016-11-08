import collections

d1 = {'spam': 1}
d2 = {'ham': 2}

c = collections.ChainMap(d1, d2)
print(c['spam'], c['ham'])

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

d4 = collections.defaultdict(value, spam=100)
print(d4)
print(d4['ham'])

d5 = collections.defaultdict(int)
print(d5['spam'])

d5['spam'] += 100
print(d5)

d6 = collections.defaultdict(list)
d6['spam'].append(100)
d6['spam'].append(200)
print(d6)
