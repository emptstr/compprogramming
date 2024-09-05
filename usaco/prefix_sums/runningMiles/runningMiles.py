t = int(input())

for _ in range(t):
    n = int(input())
    sights = list(map(int, input().split()))

    best_left = [0 for _ in range(n)]
    best_right = [0 for _ in range(n)]

    for i in range(0, n):
        best_left[i] = sights[i] + i
        best_right[i] = sights[i] - i
        
    for i in range(1,n):
        best_left[i] = max([best_left[i], best_left[i-1]])
    for i in range(n-2, -1):
        best_right[i] = max([best_right[i], best_right[i+1]])

    best_beauty = 0
    for x in range(1, n-1):
        best_beauty = max([best_beauty, best_left[x-1] + best_right[x+1] + sights[x]])

    print(best_beauty)