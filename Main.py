solved = False
# 0 = still possible path
# 1 = not possible path
# 2 = island
my_map = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 2],
    [0, 0, 2, 2]
]
ordered_move_list = []


def print_map(var=[]):
    for rw in var:
        print(rw)


def recurse(row, col, move_list):
    list_copy = []
    for direction in move_list:
        list_copy.append(direction)
    if len(list_copy) > 0:
        direction = list_copy.pop(0)
        if direction == "U" or direction == "u":
            try:
                if my_map[row - 1][col] == 2 or row - 1 < 0:
                    # print("This runs up into an island")
                    return False
                elif my_map[row - 1][col] == 0 or my_map[row - 1][col] == 1:
                    return recurse(row - 1, col, list_copy)
            except IndexError:
                # print("Index Error Here!")
                return False
        elif direction == "D" or direction == "d":
            try:
                if my_map[row + 1][col] == 2 or row + 1 > len(my_map[row]) - 1:
                    # print("This runs down into an island")
                    return False
                elif my_map[row + 1][col] == 0 or my_map[row + 1][col] == 1:
                    return recurse(row + 1, col, list_copy)
            except IndexError:
                # print("Index Error Here!")
                return False
        elif direction == "L" or direction == "l":
            try:
                if my_map[row][col - 1] == 2 or col - 1 < 0:
                    # print("This runs left into an island or off the map")
                    return False
                elif my_map[row][col - 1] == 0 or my_map[row][col - 1] == 1:
                    return recurse(row, col - 1, list_copy)
            except IndexError:
                # print("Index Error Here!")
                return False
        elif direction == "R" or direction == "r":
            try:
                if my_map[row][col + 1] == 2 or col + 1 > len(my_map[row]) - 1:
                    # print("The following position runs right into an island or off the map")
                    return False
                elif my_map[row][col + 1] == 0 or my_map[row][col + 1] == 1:
                    return recurse(row, col + 1, list_copy)
            except IndexError:
                # print("Index Error Here!")
                return False
    return True


def check_map():
    possibilities = 0
    i = 0
    while i < len(my_map):
        j = 0
        while j < len(my_map[i]):
            works_at_position = recurse(i, j, ordered_move_list)
            if works_at_position:
                possibilities += 1
            # print("The path works starting at: " + str(i) + ", " + str(j)
            #       + " : " + str(works_at_position))
            j += 1
        i += 1
    if possibilities > 1:
        return "no solution"
    else:
        i = 0
        while i < len(my_map):
            j = 0
            while j < len(my_map[i]):
                works_at_position = recurse(i, j, ordered_move_list)
                if works_at_position:
                    return str(i) + ", " + str(j)
                # print("The path works starting at: " + str(i) + ", " + str(j)
                #       + " : " + str(works_at_position))
                j += 1
            i += 1


print_map(my_map)
while check_map() == "no solution":
    print("Previously Overheard: ", end="")
    for move in ordered_move_list:
        print(move, end="")
    which_direction = input("\nWhat direction? U, D, L, R?: ")
    ordered_move_list.append(which_direction)
    if check_map() != "no solution":
        print(check_map())

