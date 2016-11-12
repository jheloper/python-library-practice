import os.path
from pathlib import Path, PurePath

# 절대경로.
print(os.path.abspath('.'))

# 여러 경로 결합.
path = os.path.join('hoge', 'fuga', 'piyo')
print(path)

# 경로 맨 끝 파일 이름 반환.
print(os.path.basename(path))

# 경로 맨 끝 파일 이름을 제외한 디렉토리 부분 반환.
print(os.path.dirname(path.encode()))

print(os.path.exists(path))

# 문자열과 바이트를 동시에 지정할 수 없음. TypeError: 'in <string>' requires string as left operand, not int
# os.path.join('hoge', 'fuga', b'piyo')

# dirname 부분과 basename 부분으로 분해.
print(os.path.split(path))

# Path : 구상 경로 클래스.
print(Path('.'))

# PurePath : 순수 경로 클래스. / 연산을 통해 경로를 결합할 수 있다.
p = PurePath('/hoge/fuga')
p /= 'piyo.txt'

print(p)

# drive : 드라이브 문자 반환. PosixPath인 경우는 빈 문자를 반환.
print(p.drive)

print(p.root)

# anchor : 드라이브와 루트를 결합한 문자열 반환.
print(p.anchor)

# parents : 경로의 상위 경로 시퀀스.
print(list(p.parents))

print(p.parent)

print(p.name)

print(p.suffix)

# stem : 경로의 맨 끝에서 확장자를 뺀 값.
print(p.stem)

# is_absolute : 절대경로 여부 반환.
print(p.is_absolute())

# joinpath : 경로에 파라미터로 주어진 경로를 연결.
print(p.joinpath('foo', 'bar', 'baz'))

print(p.match('piyo.*'))

p2 = Path.cwd() / 'newfile.txt'
print(p2.exists())

f = p2.open('w+')
print(p2.exists())

# resolve : 경로를 절대경로로 하고, 심볼릭 링크를 해제함.
print(p2.resolve())

p3 = Path('.')
print(p3.iterdir())

print(sorted(p3.iterdir()))

# glob : 경로가 가리키는 디렉토리 아래에 파라미터로 주어진 패턴에 일치하는 파일을 반환.
print(p3.glob('**/*.txt'))

print(sorted(p3.glob('**/*.txt')))
