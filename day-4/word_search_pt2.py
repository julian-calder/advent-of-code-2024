def check_forward_slash(rows, y_coord, x_coord):
    if rows[y_coord - 1][x_coord - 1] == "M":
        if rows[y_coord + 1][x_coord + 1] == "S":
            return True

    if rows[y_coord - 1][x_coord - 1] == "S":
        if rows[y_coord + 1][x_coord + 1] == "M":
            return True

    return False

def check_back_slash(rows, y_coord, x_coord):
    if rows[y_coord + 1][x_coord - 1] == "M":
        if rows[y_coord - 1][x_coord + 1] == "S":
            return True
    if rows[y_coord + 1][x_coord - 1] == "S":
        if rows[y_coord - 1][x_coord + 1] == "M":
            return True

    return False

def main():
    
    XMAS_COUNT = 0

    file = open('input.txt', 'r')
    rows = []
    for line in file:
        rows.append(line)

    for row in range(len(rows)):
        for col in range(len(rows[0])):
            if rows[row][col] == "A":
                if 0 < row < (len(rows) - 1) and 0 < col < (len(rows[0]) - 1):
                    if check_forward_slash(rows, row, col) and check_back_slash(rows, row, col):
                        XMAS_COUNT += 1

    print("Part 2: " + str(XMAS_COUNT))

if __name__ == "__main__":
    main()
