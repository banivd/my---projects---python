# "Tic - Tac - Toe." Finish.
input_cells = 9 * " "
str_char = ""
matrix = [[input_cells[3 * i + j] for j in range(3)] for i in range(3)]

# This method is drawing a game field. // input_str - is string
def draw_game_field(input_str):
    mass = []
    str_star = 9 * "-"

    print(str_star)

    for i in range(3):
        mass.append([])
        for j in range(3):
            mass[i].append(input_str[3 * i + j])
    for string in mass:
        str_mass = "|"
        for letter in string:
            str_mass += " " + letter
        str_mass += " |"
        print(str_mass)

    print(str_star)

# This method will return truth (True) or lie (False). // string - is string
def is_digit(string):
    if string.isdigit():
        return True
    else:
        return False


def input_xo(symbol):
    while True:
        input_xy = input("Enter the coordinates: > ")
        xy_ = input_xy.title().replace(' ', '')
        input_list = input_xy.split()
        if not is_digit(xy_):
            print("You should enter numbers!")
        else:
            x = int(input_list[0])
            y = int(input_list[1])
            if not(0 < x < 4 and 0 < y < 4):
                print("Coordinates should be from 1 to 3!")
            elif matrix[3 - y][x - 1] == "X" or matrix[3 - y][x - 1] == "O":
                print("This cell is occupied! Choose another one!")
            else:
                matrix[3 - y][x - 1] = symbol
                break

def convert_list_tostring(input_list):
    str_matrix = ""
    for string in input_list:
        for letter in string:
            str_matrix += letter
        str_matrix += ""
    return str_matrix

def game_analysis(mass):
    n_x = 0
    n_o = 0
    global str_char

    x_win = mass[0][0] == mass[1][1] == mass[2][2] == "X" \
            or mass[0][2] == mass[1][1] == mass[2][0] == "X" \
            or mass[0][0] == mass[0][1] == mass[0][2] == "X" \
            or mass[1][0] == mass[1][1] == mass[1][2] == "X" \
            or mass[2][0] == mass[2][1] == mass[2][2] == "X" \
            or mass[0][0] == mass[1][0] == mass[2][0] == "X" \
            or mass[0][1] == mass[1][1] == mass[2][1] == "X" \
            or mass[0][2] == mass[1][2] == mass[2][2] == "X"

    o_win = mass[0][0] == matrix[1][1] == mass[2][2] == "O" \
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
    if abs_xo == 0:
        str_char = "X"
    if abs_xo == 1:
        str_char = "O"

    if n_o == 0 and n_x == 0:
        return True
    if x_win and not o_win and n_x <= 5 and abs_xo <= 1:
        print("X wins")
        return False
    if o_win and not x_win and n_o <= 5 and abs_xo <= 1:
        print("O wins")
        return False
    if not x_win and not o_win and (n_x + n_o) == 9:
        print("Draw")
        return False
    if not x_win and not o_win and abs_xo <= 1 and (0 < n_x + n_o < 9):
        return True

draw_game_field(input_cells)

while game_analysis(matrix):
    input_xo(str_char)
    draw_game_field(convert_list_tostring(matrix))
