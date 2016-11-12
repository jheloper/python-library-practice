from dateutil.rrule import rrule
from dateutil.rrule import DAILY, WEEKLY, MONTHLY
from dateutil.rrule import MO, TU, WE, TH, FR, SA, SU
import pprint
import sys
from datetime import datetime

sys.displayhook = pprint.pprint
start = datetime(2015, 6, 28)

# rrule을 통해 반복 규칙 지정.
pprint.pprint(list(rrule(DAILY, count=5, dtstart=start)))

pprint.pprint(list(rrule(DAILY, dtstart=start, until=datetime(2015, 7, 1))))

# wkst는 주의 시작을 어떤 요일로 할 것인지 지정.
pprint.pprint(list(rrule(WEEKLY, count=8, wkst=SU, byweekday=(TU, TH), dtstart=start)))

# 매월 마지막 금요일.
pprint.pprint(list(rrule(MONTHLY, count=3, byweekday=FR(-1), dtstart=start)))

# 격주.
pprint.pprint(list(rrule(WEEKLY, count=3, interval=2, dtstart=start)))
