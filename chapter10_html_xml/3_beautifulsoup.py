from bs4 import BeautifulSoup
from urllib import request
import re

html = BeautifulSoup(request.urlopen('https://www.python.org'), 'html.parser')
print(html.title)

print(html.title.text)

print(html.h1)

print(html.find('h1'))

print(html.h1.img)

print(html.h1.img.attrs)

print(html.h1.img['src'])

print(html.find(id='back-to-top-1'))

print(html.find('li', attrs={'class': 'shop-meta'}))

url_list = html.find_all('a')
for url in url_list:
    print(url['href'])

docs_list = html.find_all(href=re.compile('^http(s)?://docs'), limit=2)
for doc in docs_list:
    print(doc['href'])

tag = html.find('div', attrs={'id': 'nojs'})
print(tag)

print(tag.get_text(strip=True))

print(tag.get_text(separator='-- '))

print(html.h1)

print(html.h1.prettify())

print(html.h1.a.prettify(formatter='html'))

html.h1.insert(0, 'ham')
print(html.h1)

html.h1.insert(3, 'egg')
print(html.h1)

new_tag = html.new_tag('span')
new_tag.string = 'ham egg'
print(html.h1.img.replace_with(new_tag))

print(html.h1)

html.h1.span.clear()
print(html.h1)

html.h1.span.decompose()
print(html.h1)

print(html.h1.a.extract())
print(html.h1)

wrapper_tag = html.new_tag('div')
