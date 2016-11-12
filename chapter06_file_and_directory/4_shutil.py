import shutil

# ignore_patterns : 무시할 파일을 패턴으로 지정.
ignore = shutil.ignore_patterns('*.pyc', '*.swp')
print(ignore)

print(shutil.copytree('./from', './to', ignore=ignore))

print(shutil.rmtree('./to'))

print(shutil.make_archive(base_name='example', format='gztar', root_dir='.', base_dir='example'))

print(shutil.unpack_archive(filename='example.tar.gz', extract_dir='./extract'))

print(shutil.move('./example.tar.gz', './extract/example'))

print(shutil.rmtree('./extract/example'))
