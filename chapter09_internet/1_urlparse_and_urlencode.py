from urllib import parse

result = parse.urlparse('https://www.python.org/doc/;parameter?q=example#hoge')
print(result)

print(result.geturl())

print(result.scheme)

print(result[0])

print(result.hostname)

result2 = parse.urlparse('https://www.google.co.kr/search?q=python&oq=python&sourceid=chrome&ie=8')

print(result2.query)

print(parse.parse_qs(result2.query))

print(parse.parse_qs('key=1&key=2'))

print(parse.parse_qsl(result2.query))

print(parse.parse_qsl('key=1&key=2'))

print(parse.parse_qs('key1=&key2=hoge'))

print(parse.parse_qs('key1=&key2=hoge', keep_blank_values=True))

print(parse.urlencode({'key1': 1, 'key2': 2, 'key3': '파이썬'}))

print(parse.urlencode([('key1', 1), ('key2', 2), ('key3', '파이썬')]))

query = {'key1': 'hoge', 'key2': ['fuga', 'piyo']}
print(parse.urlencode(query))

print(parse.urlencode(query, doseq=True))
