import xml.etree.ElementTree as et

tree = et.parse('sample.xml')
seoul = tree.find('./local_weather')
print(seoul.tag)
print(seoul.attrib)
print(seoul.get('name'))

seoul_condition = seoul.find('./condition')
print(seoul_condition.tag)
print(seoul_condition.text)

busan_condition = tree.find('./local_weather[@name="Busan"]/condition')
print(busan_condition.text)

elements = tree.findall('./local_weather')
for element in elements:
    print(element.attrib)
