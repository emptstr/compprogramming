## Marking
# instead of keeping track of the state
# of the stacks after applying each instruction
# we can mark where each interval starts using a 1 and stops using a -1
# then we simply count the number of open intervals per stack to derive our
# end state
N,K = map(int, input().split())
instructions = [tuple(map(int, input().split())) for _ in range(K)]
stacks = [0 for _ in range(N+2)]
for i in instructions: # Mark the intervals - O(n)
    stacks[i[0]] += 1
    stacks[i[1]+1] -= 1

counts = [0 for _ in range(N+1)]
open_intervals = 0
for i in range(N+2): # Derive the stack state - O(n)
    counts[i] += stacks[i]

counts.sort() # Sort - O(N log(N))
print(counts[N//2]) # Find the median
