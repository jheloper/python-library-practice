import zlib
import gzip
import bz2
import lzma

text = '한국어 텍스트'
b = text.encode('utf-8')
compressed_text = zlib.compress(b)
print(len(b))
print(len(compressed_text))

long_text = b'A' * 10000
compressed_long_text = zlib.compress(long_text)
print(len(long_text), len(compressed_long_text))

decompressed_long_text = zlib.decompress(compressed_long_text)
print(len(decompressed_long_text))

print(long_text == decompressed_long_text)

with gzip.open('sample.gz', 'wt') as f:
    f.write('한국어 텍스트를 gzip 압축 파일로 쓰기.')

with gzip.open('sample.gz', 'rt') as f:
    content = f.read()

print(content)

gzipped_data = gzip.compress(b)
print(len(b), len(gzipped_data))

gzipped_long_data = gzip.compress(long_text)
print(len(long_text), len(gzipped_long_data))

gunzipped_long_data = gzip.decompress(gzipped_long_data)
print(len(gunzipped_long_data))

print(long_text == gunzipped_long_data)

with bz2.open('sample.bz2', 'wt') as f:
    f.write('한국어 텍스트를 bzip2 압축 파일로 쓰기.')

with bz2.open('sample.bz2', 'rt') as f:
    content = f.read()

print(content)

with lzma.open('sample.xz', 'wt') as f:
    f.write('한국어 텍스트를 lzma 압축 파일로 쓰기.')

with lzma.open('sample.xz', 'rt') as f:
    content = f.read()

print(content)
