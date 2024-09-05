num_algorithms, time_to_study = map(int, input().split())
algorithms = list(map(int, input().split()))

algorithms.sort()
algorithms_studied = 0
minutes_remaining = time_to_study

for i in range(num_algorithms):
    if algorithms[i] <= minutes_remaining:
        minutes_remaining -= algorithms[i]
        algorithms_studied +=1

print(algorithms_studied)
