import array

# array.array : 갱신 가능한 시퀀스. 객체 생성 시 지정한 종류의 수치 데이터만 저장. 이진 데이터로 저장되기 때문에,
# 리스트나 튜플 등과 비교할 때 메모리 효율이 뛰어남.
arr1 = array.array('f', [1, 2, 3, 4])
print(arr1)

arr1.append(100.0)
arr1[2] = 200.
print(arr1)

del arr1[-1]
print(arr1)
print(sum(arr1))

arr2 = array.array('i', (1, 2, 3, 4, 5))
# tofile을 통해 이진 데이터를 파일에 쓰기.
with open('bin-int', 'wb') as f:
    arr2.tofile(f)

# fromfile을 통해 파일의 이진 데이터를 읽기.
with open('bin-int', 'rb') as f:
    arr2.fromfile(f, 5)

print(arr2)
