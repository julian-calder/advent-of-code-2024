import re

def main():

    total_sum = 0

    file = open('input.txt', 'r')
    text = file.read()
    regex = "mul[(][0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9][)]"
    instructions = re.findall(regex, text)
    
    for instruction in instructions:
        num_regex = r"\d+"
        nums = re.findall(num_regex, instruction)
        total_sum += (int(nums[0]) * int(nums[1]))

    print("Part 1: " + str(total_sum))

    regex_pt2 = "mul[(][0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9][)]|do[(][)]|don't[(][)]"

    instructions_pt2 = re.findall(regex_pt2, text)

    convoluted_sum = 0

    do_mul = True

    for instruction in instructions_pt2:
        if instruction == "do()":
            do_mul = True
        elif instruction == "don't()":
            do_mul = False
        else:
            if do_mul:
                num_regex = r"\d+"
                nums = re.findall(num_regex, instruction)
                convoluted_sum += (int(nums[0]) * int(nums[1]))

    print("Part 2: " + str(convoluted_sum))

if __name__ == "__main__":
    main()
