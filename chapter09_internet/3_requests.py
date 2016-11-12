import requests

r1 = requests.get('http://httpbin.org/get')
print(r1.status_code)
print(r1.text)

r2 = requests.get('http://httpbin.org/get', params='example')
print(r2.url)

r3 = requests.get('http://httpbin.org/get', params={'key': 'value'})
print(r3.url)

headers = {'Accept': 'application/json'}
r4 = requests.get('http://httpbin.org/get', headers=headers)

if requests.head(r4.url):
    print(r4.request.headers)
    print(r4.json())
else:
    print(r4.status_code)

payload = {'hoge': 'fuga'}
r5 = requests.post('http://httpbin.org/post', data=payload)
print(r5.request.body)
