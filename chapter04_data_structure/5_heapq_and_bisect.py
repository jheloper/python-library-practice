import heapq
import bisect

# 힙 큐로 사용할 리스트 필요.
queue1 = []

# heapq.heappush : 힙 큐 리스트에 요소를 추가함.
heapq.heappush(queue1, 2)
heapq.heappush(queue1, 1)
heapq.heappush(queue1, 0)
print(queue1)

# heapq.heappop : 힙 큐 리스트에서 최소값을 삭제하고 그 값을 반환.
print(heapq.heappop(queue1))
heapq.heappop(queue1)
print(queue1)

queue2 = [1, 2, 3, 4, 5]

# heapq.heapify : 리스트를 힙 큐로 정렬함.
heapq.heapify(queue2)
print(queue2)

# heapq.heappushpop : 힙 큐에 요소를 추가한 후 최소값을 빼냄.
print(heapq.heappushpop(queue2, 6))
print(queue2)
print(heapq.heappushpop(queue2, 0))
print(queue2)

queue3 = [1, 2, 3, 4, 5]

# heapq.heapreplace : 힙 큐에서 최소값을 빼낸 후 요소를 추가함. heappushpop과 처리순서가 반대임.
print(heapq.heapreplace(queue3, 0))
print(queue3)

seq1 = [0, 1, 2, 2, 3, 4, 5]
# bisect.bisect_left : 이진 탐색. 시퀀스에서 두번째 파라미터의 값을 찾는다. 같은 값이 있을 경우 가장 처음 요소의 인덱스를 반환.
print(bisect.bisect_left(seq1, 2))

# bisect.bisect_right : 이진 탐색. bisect_left와 동일하나, 같은 값이 있을 경우 가장 마지막 요소의 다음 인덱스를 반환.
print(bisect.bisect_right(seq1, 2))

seq2 = [0, 1, 2, 3, 4, 5]
# bisect.insort_left : 정렬된 시퀀스에 알맞은 위치에 요소를 삽입. bisect_left 기준으로 구한 인덱스 위치에 요소를 삽입함.
bisect.insort_left(seq2, 3)
print(seq2)
