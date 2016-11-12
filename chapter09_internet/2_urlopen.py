from urllib import request

res = request.urlopen('http://httpbin.org/get')
print(res.code)
print(res.read())

res2 = request.urlopen('http://httpbin.org/get?key1=value1')
print(res2.read())

headers = {'Accept': 'application/json'}
print(request.urlopen(request.Request('http://httpbin.org/get', headers=headers)).read())

data = 'key1=value1&key2=value2'
res3 = request.urlopen('http://httpbin.org/post', data=data.encode())
print(res3.read())

req = request.Request('http://httpbin.org/get', method='HEAD')
res4 = request.urlopen(req)
print(res4.code)
print(res4.read())
