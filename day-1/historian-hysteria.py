def main():
    list1 = []
    list2 = []

    val_dict = {}

    total_distance = 0
    similarity_score = 0

    file = open('input.txt', 'r')

    for row in file:
        vals = row.split()
        list1.append(int(vals[0]))
        list2.append(int(vals[1]))

    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])

    print("part 1: " + str(total_distance))


    for val in list1:
        val_dict[val] = 0

    for val in list2:
        if val in val_dict:
            val_dict[val] += 1

    for val, count in val_dict.items():
        similarity_score += (val * count)

    print("part 2: " + str(similarity_score))
    

if __name__ == '__main__':
    main()