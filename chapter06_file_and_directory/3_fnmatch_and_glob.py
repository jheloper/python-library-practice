import fnmatch
import re
import glob

pattern = 'hoge??.py'

# fnmatch : 파일명과 pattern 일치 여부 반환.
print(fnmatch.fnmatch('Hoge01.py', pattern))

# fnmatchcase : 기본적으로 fnmatch와 동일하나 대소문자 구분.
print(fnmatch.fnmatchcase('Hoge10.py', pattern))

# filter : 파일명 리스트로부터 pattern과 일치하는 요소만 반환.
print(fnmatch.filter(['hoge.py', 'hoge00.py', 'hoge01.py', 'fuga01.py'], pattern))

# translate : pattern을 정규표현식으로 변환.
trans_pattern = fnmatch.translate(pattern)
print(trans_pattern)

re_pattern = re.compile(trans_pattern)
print(re_pattern.match('hogege.py'))

# glob : 파라미터에 주어진 패턴과 일치하는 파일이나 디렉토리 리스트를 반환.
print(glob.glob('./*.txt'))

# iglob : glob과 같은 내용을 리스트가 아닌 제네레이터로 반환.
print(glob.iglob('./*.txt'))

# 특수 문자를 이스케이프함.
print(glob.escape('example?.txt'))
