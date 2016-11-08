import collections

d1 = collections.OrderedDict()
d1['spam'] = 100
d1['ham'] = 200
print(d1)

# 등록순서가 정해져 있음.
d2 = collections.OrderedDict([('spam', 100), ('ham', 200)])
print(d2)

# 등록순서가 정해져 있지 않음.
d3 = collections.OrderedDict({'spam': 100, 'ham': 200})
print(d3)

# 등록순서가 정해져 있지 않음.
d4 = collections.OrderedDict(spam=100, ham=200)
print(d4)

Coordinate = collections.namedtuple('Coordinate', 'X, Y, Z')
c1 = Coordinate(100, -50, 200)
print(c1)
print(c1.X)
