# "Tic - Tac - Toe." Step N2
input_cells = input("Enter cells: > ")
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


def input_x():
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
                matrix[3 - y][x - 1] = "X"
                break

def convert_list_tostring(input_list):
    str_matrix = ""
    for string in input_list:
        for letter in string:
            str_matrix += letter
        str_matrix += ""
    return str_matrix

draw_game_field(input_cells)
input_x()

draw_game_field(convert_list_tostring(matrix))
