# "Tic - Tac - Toe." Step N1
input_cells = input("Enter cells: > ")
str_star = 9 * "-"
print(str_star)

mass = []

for i in range(3):
    mass.append([])
    for j in range(3):
        mass[i].append(input_cells[3 * i + j])

for string in mass:
    str_mass = "|"
    for letter in string:
        str_mass += " " + letter
    str_mass += " |"
    print(str_mass)

print(str_star)

n_x = 0
n_o = 0

x_win = mass[0][0] == mass[1][1] == mass[2][2] == "X" \
        or mass[0][2] == mass[1][1] == mass[2][0] == "X" \
        or mass[0][0] == mass[0][1] == mass[0][2] == "X" \
        or mass[1][0] == mass[1][1] == mass[1][2] == "X" \
        or mass[2][0] == mass[2][1] == mass[2][2] == "X" \
        or mass[0][0] == mass[1][0] == mass[2][0] == "X" \
        or mass[0][1] == mass[1][1] == mass[2][1] == "X" \
        or mass[0][2] == mass[1][2] == mass[2][2] == "X"

o_win = mass[0][0] == mass[1][1] == mass[2][2] == "O" \
        or mass[0][2] == mass[1][1] == mass[2][0] == "O" \
        or mass[0][0] == mass[0][1] == mass[0][2] == "O" \
        or mass[1][0] == mass[1][1] == mass[1][2] == "O" \
        or mass[2][0] == mass[2][1] == mass[2][2] == "O" \
        or mass[0][0] == mass[1][0] == mass[2][0] == "O" \
        or mass[0][1] == mass[1][1] == mass[2][1] == "O" \
        or mass[0][2] == mass[1][2] == mass[2][2] == "O"

for i in range(3):
    for j in range(3):
        if mass[i][j] == "X":
            n_x += 1
        if mass[i][j] == "O":
            n_o += 1
abs_xo = abs(n_x - n_o)

if abs_xo >= 2:
    print("Impossible")
if x_win and o_win and abs_xo == 1:
    print("Impossible")
if x_win and not o_win and n_x <= 5 and abs_xo <= 1:
    print("X wins")
if o_win and not x_win and n_o <= 5 and abs_xo <= 1:
    print("O wins")
if not x_win and not o_win and (n_x + n_o) == 9:
    print("Draw")
if not x_win and not o_win and abs_xo <= 1 and (0 < n_x + n_o < 9):
    print("Game not finished")
