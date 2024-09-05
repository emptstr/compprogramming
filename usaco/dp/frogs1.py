N = int(input())
stone_heights = list(map(int, input().split()))
best_height = [0 for _ in range(N)]
best_height[0] = 0
best_height[1] = abs(stone_heights[0] - stone_heights[1])
for i in range(2, N):
    best_height[i] = min([best_height[i-2] + abs(stone_heights[i-2] - stone_heights[i]), best_height[i-1] + abs(stone_heights[i-1] - stone_heights[i])])

print(best_height[N-1])