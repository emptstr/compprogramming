input = open('div7.in', 'r')
N = int(input.readline())
cows = [0] + [int(input.readline()) for _ in range(N)] # used a 1-based array for simplicity
input.close()

prefix_sums = [0 for _ in range(N+1)]
for i in range(1, N+1):
    prefix_sums[i] = prefix_sums[i-1] + cows[i]

largest_group = 0
for i in range(1, N+1):
    for j in range(i+largest_group, N+1): # a slight optimization.  If we've found a group of size n there is no reason to check groups of a smaller size.
        if (prefix_sums[j] - prefix_sums[i-1]) % 7 == 0:
            largest_group = max([largest_group, (j-i)+1])

output = open('div7.out', 'w')
output.write(str(largest_group))
output.close()