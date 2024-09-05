
input_file = open('bcount.in', 'r')
COW_COUNT, QUERY_COUNT = map(int, input_file.readline().split())
cows = [int(input_file.readline()) for _ in range(COW_COUNT)]

sums = [[0 for _ in range(COW_COUNT+1)] for _ in range(4)]
for cow_type in range(1,4):
    for cow_num in range(1, COW_COUNT+1):
        count = 1 if cows[cow_num-1] == cow_type else 0
        sums[cow_type][cow_num] = sums[cow_type][cow_num-1] + count

output_file = open('bcount.out', 'w')
for _ in range(QUERY_COUNT):
    lo, hi = map(int, input_file.readline().split())
    line = " ".join([str(sums[cow_type][hi] - sums[cow_type][lo-1]) for cow_type in range(1,4)])
    output_file.write(line + "\n")

output_file.close()
input_file.close()