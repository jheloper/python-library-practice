import zipfile

print(zipfile.is_zipfile('sample/python-3.4.5-docs-text.zip'))

print(zipfile.is_zipfile('sample/python-3.4.5-docs-text.tar.bz2'))

zip = zipfile.ZipFile('sample/python-3.4.5-docs-text.zip')
print(len(zip.namelist()))

print(zip.namelist()[:2])

f = zip.open('python-3.4.5-docs-text/contents.txt')
contents = f.read()
print(contents[:60])

for name in zip.namelist():
    if 'zipfile' in name:
        zipfile_doc = name

print(zipfile_doc)

zipinfo = zip.getinfo(zipfile_doc)
print(zipinfo.filename, zipinfo.date_time)

zip.extract(zipinfo)

zip.extractall()

zip.close()

wzip = zipfile.ZipFile('example.zip', mode='w')
wzip.write('python-3.4.5-docs-text/library/zipfile.txt', 'zipfile.txt')
print(wzip.namelist())

wzip.writestr('test.txt', b'test text')
print(wzip.namelist())

wzip.close()
print(zipfile.is_zipfile('example.zip'))
