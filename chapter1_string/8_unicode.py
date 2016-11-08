import unicodedata

print(unicodedata.lookup('LATIN SMALL LETTER A'))

# 에러 발생. KeyError: "undefined character name 'UNKNOWN CHARACTER'"
# print(unicodedata.lookup('UNKNOWN CHARACTER'))

for char in ('A', 'A', '1', '1', 'ㄱ', '가'):
    print(unicodedata.name(char))

# normalize 함수를 통해 유니코드 문자열을 정규화할 수 있음. 포맷은 NFC, NFKC, NFD, NFKD.
print(unicodedata.normalize('NFC', '한글AＡ!!@＠'))

print(unicodedata.normalize('NFKC', '한글AＡ!!@＠'))
