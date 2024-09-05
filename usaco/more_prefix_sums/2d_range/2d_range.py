
N,Q = map(int, input().split())
forest = [input() for _ in range(N)]

prefixSums = [[0 for _ in range(N+1)] for _ in range(N+1)]
for row in range(1,N+1):
    prefixSum = 0
    for col in range(1,N+1):
        if forest[row-1][col-1] == '*':
            prefixSum+=1
        prefixSums[row][col] = prefixSum

for _ in range(Q):
   y1,x1,y2,x2 = map(int, input().split())
   rectangle_sum = 0
   for row in range (y1,y2+1):
       rectangle_sum += prefixSums[row][x2] - prefixSums[row][x1-1]
   print(rectangle_sum)