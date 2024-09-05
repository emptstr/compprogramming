n = int(input())
nums = list(map(int, input().split()))

prefixSum = 0
minPrefixSum = 0
best = nums[0]
for i in range(n):
    prefixSum += nums[i]
    best = max([best, prefixSum - minPrefixSum])
    minPrefixSum = min([minPrefixSum, prefixSum])

print(best)