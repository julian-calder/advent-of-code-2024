def check_safe_increasing(vals):
    # check to see if a single combination is safe.
    for i in range(len(vals) - 1):
        if (0 < int(vals[i+1]) - int(vals[i]) < 4):
            continue
        else:
            return False
    return True

def check_safe_decreasing(vals):
    # check to see if a single combination is safe.
    for i in range(len(vals) - 1):
        if (0 < int(vals[i]) - int(vals[i+1]) < 4):
            continue
        else:
            return False
    return True

def main():
    num_safe = 0

    file = open('input.txt', 'r')

    for row in file:
        num_unsafe_increasing = 0
        num_unsafe_decreasing = 0

        vals = row.split()

        # if list is already safe, don't bother splitting 
        if check_safe_increasing(vals) or check_safe_decreasing(vals):
            num_safe += 1

        else:
            # iterate through all possible sublists, removing one element from the list at a time
            for i in range(len(vals)):
                sublist = vals[0:i] + vals[i+1:]

                if check_safe_increasing(sublist):
                    # if we have a combination that is safe
                    num_safe += 1
                    break
                elif check_safe_decreasing(sublist):
                    num_safe += 1
                    break

    print("part 2: " + str(num_safe))

if __name__ == '__main__':
    main()
