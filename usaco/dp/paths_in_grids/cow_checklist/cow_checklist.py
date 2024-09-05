input_file = open('checklist.in', 'r')
H,G = map(int, input_file.readline().split())
holsteins = [tuple(map(int, input_file.readline().split())) for _ in range(H)]
guerneys = [tuple(map(int, input_file.readline().split())) for _ in range(G)]
input_file.close()

HOLSTEIN_PICKED = 0
GUERNEY_PICKED = 1

def distance(first_cow, second_cow):
    return (first_cow[0]-second_cow[0])**2 + (first_cow[1]-second_cow[1])**2

state = [[[10**9,10**9] for _ in range (G+1)] for _ in range(H+1)] # state[num_holsteins][num_gueryneys][type_picked]
state[1][0][HOLSTEIN_PICKED] = 0 # we start with the first holstein
state[1][1][GUERNEY_PICKED] = distance(holsteins[0], guerneys[0])

for i in range(H+1):
    for j in range(G+1):
        if i > 1: # holstein picked
            state[i][j][HOLSTEIN_PICKED] = min([
                state[i][j][HOLSTEIN_PICKED],
                state[i-1][j][HOLSTEIN_PICKED] + distance(holsteins[i-2], holsteins[i-1]),
            ])

        if j > 1: # guerney picked
            state[i][j][GUERNEY_PICKED] = min([
                state[i][j][GUERNEY_PICKED],
                state[i][j-1][GUERNEY_PICKED] + distance(guerneys[j-2], guerneys[j-1]),
            ])

        if i > 0 and j > 0:
            state[i][j][HOLSTEIN_PICKED] = min([
                state[i][j][HOLSTEIN_PICKED],
                state[i-1][j][GUERNEY_PICKED] + distance(holsteins[i-1], guerneys[j-1])
            ])
            state[i][j][GUERNEY_PICKED] = min([
                state[i][j][GUERNEY_PICKED],
                state[i][j-1][HOLSTEIN_PICKED] + distance(holsteins[i-1], guerneys[j-1])
            ])  

out_file = open('checklist.out', 'w')
out_file.write(str(state[H][G][HOLSTEIN_PICKED]))
out_file.close()