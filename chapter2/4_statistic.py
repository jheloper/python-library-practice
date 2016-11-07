import statistics

data = [1, 2, 2, 3, 4, 5, 6]

# 평균값
print(statistics.mean(data))

# 중앙값
print(statistics.median(data))

# 최빈값
print(statistics.mode(data))

# 모표준편차
print(statistics.pstdev(data))

# 표본표준편차
print(statistics.stdev(data))

# 모분산
print(statistics.pvariance(data))

# 표본분산
print(statistics.variance(data))
