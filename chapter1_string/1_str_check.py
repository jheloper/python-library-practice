# 알파벳 & 숫자.
print('123aBc'.isalnum())

print('123abC#'.isalnum())

# 알파벳.
print('abcD'.isalpha())

print('한국어'.isalpha())

# 대문자.
print('UPPER'.isupper())

# 소문자.
print('lower'.islower())

# Title 형식.
print('Title String'.istitle())

# decimal은 10진수 숫자, digit는 숫자를 나타내는 문자, numeric은 수를 나타내는 문자열.
num1 = '1234567890'

print('%s, %s, %s' % (num1.isdecimal(), num1.isdigit(), num1.isnumeric()))

num2 = '１２３４５'

print('%s, %s, %s' % (num2.isdecimal(), num2.isdigit(), num2.isnumeric()))

num3 = '①②③④⑤'

print('%s, %s, %s' % (num3.isdecimal(), num3.isdigit(), num3.isnumeric()))

num4 = 'ⅠⅡⅢⅣⅤ'

print('%s, %s, %s' % (num4.isdecimal(), num4.isdigit(), num4.isnumeric()))

num5 = '一二三四五'

print('%s, %s, %s' % (num5.isdecimal(), num5.isdigit(), num5.isnumeric()))
