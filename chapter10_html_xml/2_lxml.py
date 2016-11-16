from lxml import etree, html
import urllib.request

parser = etree.XMLParser(recover=True)
tree = etree.parse('broken.xml', parser)
print(tree.find('./local_weather').attrib)

source = urllib.request.urlopen('https://docs.python.org/3.4/library/index.html').read()
tree2 = etree.fromstring(source, etree.HTMLParser())
elements = tree2.findall('.//li[@class="toctree-l1"]/a')

for element in elements:
    print(element.text, element.attrib['href'])

url = 'https://docs.python.org/3.4/library/index.html'
tree3 = html.parse(urllib.request.urlopen(url)).getroot()
div_toctree = tree3.find('.//div[@class="toctree-wrapper compound"]/')
print(html.tostring(div_toctree, pretty_print=True, encoding='unicode'))

for tag in div_toctree.xpath('//*[@class]'):
    tag.attrib.pop('class')

absolute_url = html.make_links_absolute(div_toctree, base_url='https://docs.python.org/3.4/library/')

print(html.tostring(absolute_url, pretty_print=True, encoding='unicode'))
