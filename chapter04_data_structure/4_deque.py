import collections

deq1 = collections.deque('spam')
print(deq1)
print(deq1[1])
deq1[1] = 'P'
print(deq1)
# deque는 슬라이스 연산을 지원하지 않음. TypeError: sequence index must be integer, not 'slice'.
# print(deq1[1:-1])

deq2 = collections.deque(maxlen=5)

for v in range(10):
    deq2.append(v)
    if len(deq2) >= 5:
        print(list(deq2), sum(deq2)/5)

deq3 = collections.deque('12345')
print(deq3)

# rotate : 파라미터로 양수를 지정하면 deque의 요소가 오른쪽으로 회전, 음수를 지정하면 왼쪽으로 회전.
deq3.rotate(3)
print(deq3)
deq3.rotate(-3)
print(deq3)

# popleft : deque의 맨 앞 요소를 가져옴.
first = deq3.popleft()
print(first)
deq3.rotate(-1)
print(deq3)

# appendleft : deque의 맨 앞에 요소를 추가함.
deq3.appendleft(first)
print(deq3)
deq3.rotate(1)
print(deq3)
