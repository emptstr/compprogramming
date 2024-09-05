num_sticks = int(input())
stick_lengths = list(map(int, input().split()))

stick_lengths.sort()
median_length = stick_lengths[num_sticks//2]
cost = 0
for i in range(num_sticks):
    cost += max([median_length, stick_lengths[i]]) - min([median_length, stick_lengths[i]])

print(cost)