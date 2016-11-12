from datetime import datetime
import math

print('1 + 2 = {0}'.format(1 + 2))

a = 2
b = 3
print('{0} * {1} = {2}'.format(a, b, a * b))

print('{} is better than {}'.format('Beautiful', 'ugly'))

print('{1} is better than {0}'.format('implicit', 'Explicit'))

print('My name is {name}'.format(name='joonghyeon'))

person = {'name': 'joonghyeon',
          'google': 'joonghyeon@google.com'}
print('My google id is {google}'.format_map(person))

words = ['spam', 'ham', 'eggs']
print('I like {0[2]}'.format(words))

print('My name is {person[name]}'.format(person=person))

now = datetime.now()
print('Today is {0.year}-{0.month}-{0.day}'.format(now))

print('|{:<30}|'.format('left align'))

print('|{:>30}|'.format('right align'))

print('|{:^30}|'.format('center'))

print('{:-^30}'.format('center'))

print('{0:b} {0:o} {0:d} {0:x} {0:X}'.format(1000))

print('{0} {0:f}'.format(math.pi))

print('{:%}'.format(0.045))

print('{:,}'.format(1000000000000))

print('{:4.2f} {:2.2%}'.format(math.pi, 0.045))

print('Today is {:%Y-%m-%d}'.format(now))

print('Current time is {:%H:%M:%S}'.format(now))
