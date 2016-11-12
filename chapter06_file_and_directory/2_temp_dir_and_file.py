import tempfile
import os

# TemporaryFile : 임시파일 생성.
with tempfile.TemporaryFile() as tmp:
    print(tmp.write(b'test test test\n'))
    print(tmp.seek(0))
    print(tmp.read())

# 임시파일이 close 되었기 때문에 에러 발생. ValueError: write to closed file
# tmp.write(b'write again\n')

# NamedTemporaryFile : 이름이 있는 임시파일 생성.
tmp2 = tempfile.NamedTemporaryFile()
print(tmp2.name)

print(os.path.exists(tmp2.name))

# TemporaryDirectory : 임시 디렉토리 생성.
with tempfile.TemporaryDirectory() as dir_path:
    with tempfile.TemporaryFile(dir=dir_path) as tmp3:
        print(tmp3.name)

tmpdir = tempfile.TemporaryDirectory()
print(tmpdir)

tmpdir.cleanup()
