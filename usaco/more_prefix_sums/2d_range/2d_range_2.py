N,Q = map(int, input().split())
forest = [input() for _ in range(N)]

prefix_sums = [[0 for _ in range(N+1)] for _ in range(N+1)]
for row in range(1, N+1):
    for col in range(1, N+1):
        current_cell_count = 1 if forest[row-1][col-1] == '*' else 0
        prefix_sums[row][col] = prefix_sums[row-1][col] + prefix_sums[row][col-1] - prefix_sums[row-1][col-1] + current_cell_count

for _ in range(Q):
   y1,x1,y2,x2 = map(int, input().split())
   rectangle_sum = prefix_sums[y2][x2] - (prefix_sums[y1-1][x2] + (prefix_sums[y2][x1-1] - prefix_sums[y1-1][x1-1]))
   print(rectangle_sum)