input = open('div7.in', 'r')
N = int(input.readline())
cows = [0] + [int(input.readline()) for _ in range(N)] # used a 1-based array for simplicity
input.close()

prefix_sums = [0 for _ in range(N+1)]
for i in range(1, N+1): # calculate prefix sums - O(n)
    prefix_sums[i] = prefix_sums[i-1] + cows[i] 

largest_group = 0
for i in range(1, N+1): # calculate all possible groups (pairs of indices) - O(n^2)
    for j in range(i, N+1):
        if (prefix_sums[j] - prefix_sums[i-1]) % 7 == 0: # calculate prefix sums - O(1)
            largest_group = max([largest_group, (j-i)+1])

output = open('div7.out', 'w')
output.write(str(largest_group))
output.close()