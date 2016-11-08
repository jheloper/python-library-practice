from decimal import *

print(Decimal('1'))

print(Decimal(3.14))

print(Decimal((0, (3, 1, 4), -2)))

print(Decimal((1, (1, 4, 1, 4), -3)))

print(Decimal('1.1') - Decimal('0.1'))

x = Decimal('1.2')
y = Decimal('0.25')
print(x + y)

# TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'float'
# print(x + 1.0)

a = Decimal('10')
b = Decimal('3')
print(a / b)

# getcontext().prec 값을 통해 계산 정밀도 조정 가능.
getcontext().prec = 8
print(a / b)

# quantize()를 통해 반올림 방법 지정.
exp = Decimal((0, (1, 0), -1))
print(Decimal('1.04').quantize(exp, rounding=ROUND_UP))

print(Decimal('1.06').quantize(exp, ROUND_HALF_DOWN))

print(Decimal('1.15').quantize(exp, ROUND_HALF_EVEN))

print(Decimal('1.25').quantize(exp, ROUND_HALF_EVEN))

print(Decimal('1.26').quantize(exp, ROUND_HALF_EVEN))

print(Decimal('1.55').quantize(exp, ROUND_05UP))

print(Decimal('1.75').quantize(exp, ROUND_05UP))
