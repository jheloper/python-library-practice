import pytz
from datetime import datetime

fmt = '%Y-%m-%d %H:%M:%S %Z%z'

# 표준시간대 정보.
seoul = pytz.timezone('Asia/Seoul')
eastern = pytz.timezone('US/Eastern')

# localize로 표준시간대가 지정된 datetime 생성.
seoul_dt = seoul.localize(datetime(2015, 3, 1, 17, 22))
print(seoul_dt.strftime(fmt))

# astimezone으로 표준시간대 변경.
eastern_dt = seoul_dt.astimezone(eastern)
print(eastern_dt.strftime(fmt))

seoul_dt = seoul.localize(datetime(2015, 6, 25, 17, 22))
eastern_dt = seoul_dt.astimezone(eastern)
print(eastern_dt.strftime(fmt))

jan = datetime(2015, 1, 1)
jun = datetime(2015, 6, 1)

# utcoffsetdmfh UTC로부터 지정된 일시의 차를 반환.
print(eastern.utcoffset(jan))

print(eastern.utcoffset(jun))

# dst로 서머타임의 차를 반환.
print(eastern.dst(jan))

print(eastern.dst(jun))

# tzname으로 표준시간대 이름을 반환.
print(eastern.tzname(jan))

print(eastern.utcoffset(jun))

print(pytz.country_timezones['nz'])

print(pytz.country_names['nz'])

print(pytz.all_timezones)

print('Singapore' in pytz.all_timezones_set)

print('Singapore' in pytz.common_timezones_set)

print('Asia/Singapore' in pytz.common_timezones_set)
