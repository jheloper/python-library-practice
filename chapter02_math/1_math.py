import math

print(abs(-5.0))

print(max([1, -2, 5]))

print(min([1, -2, 5]))

print(sum([1, 2, 3.0]))

print(sum([1, 2, 3], 2))

print(pow(2, 3))

print(pow(2, 3, 6))

print(math.log(100))

# math.log의 두번째 파라미터를 밑으로 하는 로그.
print(math.log(100, 10))

# 10을 밑으로 하는 로그.
print(math.log10(100))

# 2를 밑으로 하는 로그.
print(math.log2(100))

# 거듭제곱.
print(math.pow(2, 3))

# 제곱근.
print(math.sqrt(16))

# 래디안의 사인(sin).
radian = math.radians(90)
print(math.sin(radian))

# 래디안의 코사인(cos).
radian2 = math.radians(180)
print(math.cos(radian2))

# 래디안의 코사인(cos).
print(math.tan(radian2))

print(math.ceil(3.14))

print(math.floor(3.14))

print(math.floor(-3.14))

print(math.trunc(3.14))

print(math.trunc(-3.14))

# 절댓값, abs 함수와는 달리 복소수 불가.
print(math.fabs(-3.14))

# 원주율.
print(math.pi)

# 자연로그의 밑.
print(math.e)
