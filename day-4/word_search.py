def check_up(rows, y_coord, x_coord):
    if rows[y_coord - 1][x_coord] == "M":
        if rows[y_coord - 2][x_coord] == "A":
            if rows[y_coord - 3][x_coord] == "S":
                return True
            return False
        return False
    return False

def check_down(rows, y_coord, x_coord):
    if rows[y_coord + 1][x_coord] == "M":
        if rows[y_coord + 2][x_coord] == "A":
            if rows[y_coord + 3][x_coord] == "S":
                return True
            return False
        return False
    return False

def check_left(rows, y_coord, x_coord):
    if rows[y_coord][x_coord - 1] == "M":
        if rows[y_coord][x_coord - 2] == "A":
            if rows[y_coord][x_coord - 3] == "S":
                return True
            return False
        return False
    return False

def check_right(rows, y_coord, x_coord):
    if rows[y_coord][x_coord + 1] == "M":
        if rows[y_coord][x_coord + 2] == "A":
            if rows[y_coord][x_coord + 3] == "S":
                return True
            return False
        return False
    return False


def check_up_left(rows, y_coord, x_coord):
    if rows[y_coord - 1][x_coord - 1] == "M":
        if rows[y_coord - 2][x_coord - 2] == "A":
            if rows[y_coord - 3][x_coord - 3] == "S":
                return True
            return False
        return False
    return False

def check_up_right(rows, y_coord, x_coord):
    if rows[y_coord - 1][x_coord + 1] == "M":
        if rows[y_coord - 2][x_coord + 2] == "A":
            if rows[y_coord - 3][x_coord + 3] == "S":
                return True
            return False
        return False
    return False

def check_down_left(rows, y_coord, x_coord):
    if rows[y_coord + 1][x_coord - 1] == "M":
        if rows[y_coord + 2][x_coord - 2] == "A":
            if rows[y_coord + 3][x_coord - 3] == "S":
                return True
            return False
        return False
    return False

def check_down_right(rows, y_coord, x_coord):
    if rows[y_coord + 1][x_coord + 1] == "M":
        if rows[y_coord + 2][x_coord + 2] == "A":
            if rows[y_coord + 3][x_coord + 3] == "S":
                return True
            return False
        return False
    return False

def main():
    
    XMAS_COUNT = 0

    file = open('input.txt', 'r')
    rows = []
    for line in file:
        rows.append(line)

    for row in range(len(rows)):
        for col in range(len(rows[0])):
            if rows[row][col] == "X":
                if row > 2:
                    if check_up(rows, row, col):
                        XMAS_COUNT += 1

                if col > 2:
                    if check_left(rows, row, col):
                        XMAS_COUNT += 1

                if row < (len(rows) - 3):
                    if check_down(rows, row, col):
                        XMAS_COUNT += 1

                if col < (len(rows[0]) - 4):
                    if check_right(rows, row, col):
                        XMAS_COUNT += 1

                if row > 2 and col > 2:
                    if check_up_left(rows, row, col):
                        XMAS_COUNT += 1

                if row > 2 and col < (len(rows[0]) - 4):
                    if check_up_right(rows, row, col):
                        XMAS_COUNT += 1

                if row < (len(rows) - 3) and col > 2:
                    if check_down_left(rows, row, col):
                        XMAS_COUNT += 1

                if row < (len(rows) - 3) and col < (len(rows[0]) - 4):
                    if check_down_right(rows, row, col):
                        XMAS_COUNT += 1

    print("Part 1: " + str(XMAS_COUNT))

if __name__ == "__main__":
    main()
