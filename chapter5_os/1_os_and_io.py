import os
import io
from unittest.mock import patch

print(os.environ['Path'])

# 환경변수를 설정할 수 있으나, 이 설정은 실행 중인 프로세스 상에서만 일시적으로 반영.
os.environ['TEST'] = 'good'
print(os.environ['TEST'])

# 현재 작업 디렉토리.
print(os.getcwd())

print(os.chdir('test'))

print(os.mkdir('good'))

print(os.listdir('.'))

print(os.rmdir('good'))

print(os.cpu_count())

# os 모듈 상수.
print(os.curdir)

print(os.pardir)

print(os.sep)

print(os.extsep)

print(os.linesep)

# 운영체제가 제공하는 난수 생성 함수.
print(os.urandom(10))

stream = io.StringIO('this is test\n')
print(stream.read(10))

# tell : 스트림의 현재 오프셋 반환.
print(stream.tell())

# seek : 오프셋을 지정 위치로 이동.
print(stream.seek(0, io.SEEK_END))

print(stream.write('test'))

# getvalue : 스트림의 모든 내용을 문자열로 반환.
print(stream.getvalue())

# 스트림이 닫힌 후 쓰기 동작 시 에러 발생. ValueError: I/O operation on closed file
# stream.close()
# print(stream.write('test'))


def print_hoge():
    print('hoge')


@patch('sys.stdout', new_callable=io.StringIO)
def test_print_hoge(mocked_object):
    print_hoge()
    assert mocked_object.getvalue() == 'hoge\n'

test_print_hoge()
