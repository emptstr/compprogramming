input = open('div7.in', 'r')
N = int(input.readline())
cows = [0] + [int(input.readline()) for _ in range(N)] # used a 1-based array for simplicity
input.close()

prefix_sums = [0 for _ in range(N+1)] # calculate prefix sums mod 7. There are 6 possible remainder values 0-6.  Thus if two indices have the same value their difference would have a remainder of 0.
for i in range(1, N+1):
    prefix_sums[i] = (prefix_sums[i-1] + cows[i]) % 7

largest_group = 0
first_occurence = [None for _ in range(7)]
for i in range(N+1): # find the two indicies with the same remainder value furthest apart - O(n)
    if first_occurence[prefix_sums[i]] is None:
        first_occurence[prefix_sums[i]] = i
    else:
        largest_group = max(largest_group, (i-first_occurence[prefix_sums[i]]))


output = open('div7.out', 'w')
output.write(str(largest_group))
output.close()