import tarfile

print(tarfile.is_tarfile('sample/python-3.4.5-docs-text.zip'))

print(tarfile.is_tarfile('sample/python-3.4.5-docs-text.tar.bz2'))

tar = tarfile.open('sample/python-3.4.5-docs-text.tar.bz2')
print(tar.getnames())

print(tar.getnames()[:2])

f = tar.extractfile('python-3.4.5-docs-text/contents.txt')
contents = f.read()
print(contents[:60])

for name in tar.getnames():
    if 'tarfile' in name:
        tarfile_doc = name

print(tarfile_doc)

tarinfo = tar.getmember(tarfile_doc)
print(tarinfo.name, tarinfo.size, tarinfo.mtime, tarinfo.mode)

tar.extract(tarinfo)

tar.extractall()

tar.close()

wtar = tarfile.open('example.tar.gz', mode='w:gz')
wtar.add('python-3.4.5-docs-text/library/tarfile.txt', 'tarfile.txt')
print(wtar.getnames())

wtar.close()
print(tarfile.is_tarfile('example.tar.gz'))
