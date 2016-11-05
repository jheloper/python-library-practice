import re

regex = re.compile('(\d+)-(\d+)-(\d+)')

m = regex.match('012-3456-7890')
print(m.group())

print(m.group(1), m.group(2), m.group(3))

regex2 = re.compile(r'(?P<first>\w+) (?P<last>\w+)')

m2 = regex2.match('JoongHyeon Kim: Developer')
print(m2.group(0))

print(m2.group('first'), m2.group('last'))

print(m2.groups())

print(m2.groupdict())

print(m2.expand(r'last: \2, fist: \1'))

print(m2.expand(r'last: \g<last>, fist: \g<first>'))
