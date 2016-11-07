import random

print(random.random())

# 두 파라미터 사이의 정수 난수를 생성.
print(random.randint(1, 5))

# 두 파라미터 사이의 실수 난수를 생성.
print(random.uniform(1, 5))

# random seed 지정 가능. random seed를 지정하면 이후의 random 모듈 함수가 영향을 받는다.
random.seed(10)
print(random.random())

# 특정 분포를 따르는 난수 생성.
normal_variate = []
gamma = []

for i in range(10000):
    normal_variate.append(random.normalvariate(0, 1))
    gamma.append(random.gammavariate(3, 1))

print(normal_variate)
print(gamma)

# 시퀀스에서 1개를 선택.
seq = [1, 2, 3, 4, 5]
print(random.choice(seq))

# 시퀀스에서 2개를 샘플로 추출.
print(random.sample(seq, 2))

# 시퀀스 셔플.
random.shuffle(seq)
print(seq)
