import base64

s = 'Python은 간단히 습득할 수 있으며 이와 동시에 강력한 언어 중 하나입니다.'
# print(base64.b64encode(s))
s_encode = base64.b64encode(s.encode())
print(s_encode)
print(base64.b64encode(s.encode(), altchars=b'@*'))

print(base64.b64decode(s_encode))
print(base64.b64decode(s_encode).decode())
