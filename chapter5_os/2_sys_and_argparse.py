import sys
import pprint
import argparse

# 파이썬 스크립트 실행 시 지정된 파라미터 출력.
print(sys.argv)

sys.path.append('c:\\test')
pprint.pprint(sys.path)

# print(sys.exit('프로그램 종료'))

# 표준 입출력 객체. stdin, stdout, stderr.
sys.stdout.write('standard output message\n')

sys.stderr.write('standard error message\n')

# stdin 객체는 읽기 전용이므로 쓰기를 하면 에러 발생. io.UnsupportedOperation: not writable.
# sys.stdin.write('standard input message?\n')

print(sys.stdin.read())

parser = argparse.ArgumentParser(description='Example command')

parser.add_argument('-s', '--string', type=str, help='string to display', required=True)

parser.add_argument('-n', '--num', type=int, help='number to times repeatedly display the string', default=2)

args = parser.parse_args()

print(args.string * args.num)
