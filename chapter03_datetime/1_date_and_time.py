from datetime import date, time

newyearsday = date(2017, 1, 1)
print(newyearsday)

print(newyearsday.year, newyearsday.month, newyearsday.day, newyearsday.weekday())

print(newyearsday.isoformat())

print(str(newyearsday))

# 지정한 포맷으로 날짜 문자열 반환.
print(newyearsday.strftime('%Y/%m/%d'))

print(newyearsday.strftime('%Y %b %d (%a)'))

print(date.today())

print(time())

print(time(16, 12, 25))

print(time(minute=10))

print(time(second=10))

print(time(microsecond=10))

now = time(16, 12, 25)
print(now.hour, now.minute, now.second, now.microsecond)

print(now.isoformat())

# 지정한 포맷으로 시간 문자열 반환.
print(now.strftime('%H:%M'))

print(str(now))
