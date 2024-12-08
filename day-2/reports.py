def main():
    num_safe = 0

    file = open('input.txt', 'r')

    for row in file:
        increasing = False
        safe = True

        vals = row.split()
        if int(vals[1]) > int(vals[0]):
            increasing = True

        for i in range(len(vals) - 1):
            if (increasing and (0 < int(vals[i+1]) - int(vals[i]) < 4)):
                continue
            elif (not increasing and (0 < int(vals[i]) - int(vals[i+1]) < 4)):
                continue
            else: 
                safe = False
                break
        if safe:
            num_safe+= 1

    print("part 1: " + str(num_safe))

if __name__ == '__main__':
    main()
