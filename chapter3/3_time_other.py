import time

# UTC 시간
print(time.gmtime())

# 지역 시간
print(time.localtime())

print(time.strftime('%Y-%m-%d', time.localtime()))

print(time.time())

local = time.localtime()
utc = time.gmtime()

print(local.tm_mday)

print(local.tm_hour)

print(utc.tm_hour)

for i in range(5):
    print(time.time())
    time.sleep(0.5)
