## Simulation
# directly simulate the problem
N,K = map(int, input().split())
instructions = [tuple(map(int, input().split())) for _ in range(K)]
stacks = [0 for _ in range(N+1)]
for i in instructions: # simulate each of the K instructions - O(K*N)
    for j in range(i[0], i[1]+1):
        stacks[j] +=1
stacks.sort() # sort the stacks - O(Nlog(N))
print(stacks[N // 2]) # find the median