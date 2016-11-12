import weakref
import enum

# weakref : 약한 참조 기능을 제공하는 라이브러리.
_files = weakref.WeakValueDictionary()


def share_file(filename):
    if filename not in _files:
        ret = _files[filename] = open(filename)
    else:
        ret = _files[filename]
    return ret


print(share_file('bin-int'))


# enum.Enum : 열거형 클래스. 열거형을 정의할 때 상속받아서 사용한다.
class Dynasty(enum.Enum):
    GOGURYEO = 1
    BAEKJE = 2
    SILLA = 3
    GAYA = 4

print(Dynasty.SILLA)
print(Dynasty.SILLA.name)
print(Dynasty.SILLA.value)


class Spam(enum.Enum):
    HAM = 1
    EGG = 2
    BACON = 2

# 열거형 비교 시, 같은 열거형 타입이며 값이 같다면 이름이 달라도 동일하게 취급한다.
print(isinstance(Spam.HAM, Spam))
print(Spam.HAM == Spam.HAM)
print(Spam.HAM == Spam.EGG)
print(Spam.EGG == Spam.BACON)


class Spam2(enum.Enum):
    HAM = 1
    EGG = 2
    BACON = 2

# 다른 열거형 타입끼리 비교 시 같은 값일지라도 다르게 취급한다. 또한 상수 정수와도 다르게 취급한다.
print(Spam.HAM == Spam2.HAM)
print(Spam2.HAM == 1)


# enum.unique 데코레이터를 지정하면 같은 값의 열거형은 오류 발생. ValueError: duplicate values found in <enum 'Spam3'>: EGG -> HAM
# @enum.unique
class Spam3(enum.Enum):
    HAM = 1
    EGG = 1

# 중복 값은 출력되지 않는다.
print(list(Spam2))
