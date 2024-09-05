N = int(input())
grid = [input() for _ in range(N)]
path_count = [[0 for _ in range(N)] for _ in range(N)]
for i in range(0, N):
    path_count[i][0] = 1 if grid[i][0] != '*' else 0
    path_count[0][i] = 1 if grid[0][i] != '*' else 0

for row in range(1, N):
    for col in range(1, N):
        if grid[row][col] != '*':
            path_count[row][col] = path_count[row-1][col] + path_count[row][col-1]

print(path_count[N-1][N-1]  % int(1e9 + 7))
