import sys

N, Q = map(int, sys.stdin.buffer.readline().split())
numbers = list(map(int, sys.stdin.buffer.readline().split()))
sums = [0]
sum = 0
for i in range(N):
    sum += numbers[i]
    sums.append(sum)

print

for _ in range(0, Q):
    L, R = map(int, sys.stdin.buffer.readline().split())
    print(sums[R] - sums[L])