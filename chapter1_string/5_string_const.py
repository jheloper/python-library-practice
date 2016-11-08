import string

# string 모듈에 몇 가지 문자열 상수가 정의되어 있음.
print('a' in string.ascii_lowercase)

print('a' in string.ascii_uppercase)

print('A' in string.ascii_letters)

print('123' in string.digits)

print('a' in string.hexdigits)

print('8' in string.octdigits)

print('#$' in string.punctuation)

print(' ' in string.whitespace)
