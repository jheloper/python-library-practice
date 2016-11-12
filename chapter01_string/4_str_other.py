# 파라미터 문자열이 존재하는 위치 반환, 없으면 -1.
print('python'.find('th'))

print('python'.find('TH'))

words = '''Beautiful is better than ugly.
Explicit is better than implicit.'''.split()
print(words)

# 파라미터 문자열 결합
print('-'.join(words[:5]))

print('python'.startswith('py'))

image_suffix = ('jpg', 'png', 'gif')
print('image.png'.endswith(image_suffix))

print('text.txt'.endswith(image_suffix))

# 지정한 인코딩 형식으로 변환. 두번째 파라미터로 변환 불가능한 문자열 존재시 대응방법 기술. 기본은 strict.
text = '가abc나'
# print(text.encode('ascii')) // UnicodeEncodeError

print(text.encode('ascii', 'ignore'))

print(text.encode('ascii', 'replace'))
