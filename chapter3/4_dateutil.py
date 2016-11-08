from dateutil import parser, relativedelta
from datetime import datetime, date

print(parser.parse('2015/06/23 12:34:56'))

print(parser.parse('2015-06-23'))

print(parser.parse('20150623'))

print(parser.parse('20150623123456'))

print(parser.parse('Tue, 23 Jun 2015 12:34:56 KST'))

print(parser.parse('Tue, 23 Jun 2015 12:34:56 GMT'))

# parse시 default를 지정할 수 있음.
default = datetime(2015, 7, 5)
print(parser.parse('Tue, 23 Jun 2015 12:34:56', default=default))

print(parser.parse('Tue 12:34:56', default=default))

print(parser.parse('12:34:56', default=default))

print(parser.parse('12:34', default=default))

print(parser.parse('1/2/3'))

print(parser.parse('1/2/3', dayfirst=True))

print(parser.parse('1/2/3', yearfirst=True))

now = datetime.now()
print(now)

today = datetime.today()
print(today)

# timedelta처럼 날짜 계산 가능.
print(now + relativedelta.relativedelta(months=+1))

print(now + relativedelta.relativedelta(months=-1, weeks=+1))

print(today + relativedelta.relativedelta(months=+1, hour=10))

# 다음 금요일을 찾음. 당일 포함.
print(today + relativedelta.relativedelta(weekday=relativedelta.FR))

# 이달의 마지막 금요일 찾기.
print(today + relativedelta.relativedelta(day=31, weekday=relativedelta.FR(-1)))

# 다음 화요일을 찾음, 당일 포함.
print(today + relativedelta.relativedelta(weekday=relativedelta.TU(+1)))

# 당일을 제외하고 다음 화요일을 찾음.
print(today + relativedelta.relativedelta(days=+1, weekday=relativedelta.TU(+1)))

# 해당 연도의 100일째 되는 날을 찾음. 기준이 되는 날짜를 어떻게 지정하든 무조건 1월 1일부터 셈.
print(date(2015, 1, 1) + relativedelta.relativedelta(yearday=100))

print(date(2015, 12, 31) + relativedelta.relativedelta(yearday=100))

print(date(2012, 1, 1) + relativedelta.relativedelta(yearday=100))

# 윤일을 제외하고 셈.
print(date(2012, 1, 1) + relativedelta.relativedelta(nlyearday=100))

# 두 개의 파라미터가 주어지면, 두 파라미터의 날짜 간의 차를 반환.
print(relativedelta.relativedelta(date(2015, 1, 1), today))

print(relativedelta.relativedelta(date(2016, 1, 1), today))
