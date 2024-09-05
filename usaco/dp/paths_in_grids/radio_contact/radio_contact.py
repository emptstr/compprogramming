input_file = open('radio.in', 'r')
N,M = map(int, input_file.readline().split())
f_start = tuple(map(int, input_file.readline().split()))
b_start = tuple(map(int, input_file.readline().split()))

def distance(pos_2, pos_1):
    return (pos_2[0] - pos_1[0])**2 + (pos_2[1] - pos_1[1])**2

def change_position(direction, position):
    if direction == 'N':
        return (position[0], position[1] + 1)
    elif direction == 'E':
        return (position[0]+1, position[1])
    elif direction == 'S':
        return (position[0], position[1]-1)
    else:
        return (position[0]-1, position[1])

f_moves = input_file.readline()
f_positions = [f_start]
for i in range(1, N+1):
    f_positions.append(change_position(f_moves[i-1], f_positions[i-1]))

b_moves = input_file.readline()
b_positions = [b_start]
for i in range(1, M+1):
    b_positions.append(change_position(b_moves[i-1], b_positions[i-1]))

input_file.close()
min_energy = [[10**9 for _ in range(M+1)] for _ in range(N+1)]

min_energy[0][0] = 0

for n in range(N+1):
    for m in range(M+1):
        if n > 0:
            min_energy[n][m] = min([min_energy[n][m], min_energy[n-1][m]])

        if m > 0:
            min_energy[n][m] = min([min_energy[n][m], min_energy[n][m-1]])

        if n > 0 and m > 0:
            min_energy[n][m] = min([min_energy[n][m], min_energy[n-1][m-1]])

        if n > 0 or m > 0:
            min_energy[n][m] += distance(f_positions[n], b_positions[m])

output_file = open('radio.out', 'w')
output_file.write(str(min_energy[N][M]))