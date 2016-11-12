from datetime import datetime, date, timedelta

today = datetime.today()

print(today)

print(today.date())

print(today.time())

print(today.isoformat())

# 지정한 포맷으로 일시 문자열 반환.
print(today.strftime('%Y/%m/%d'))

todaydate = date.today()

newyearsday = date(2017, 1, 1)

print(newyearsday - todaydate)

week = timedelta(days=7)

print(todaydate + week)

print(todaydate + week * 2)

print(todaydate - week)
