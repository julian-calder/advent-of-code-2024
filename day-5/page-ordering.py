import re

def check_valid(vals, rules_dict):
    # iterate through each value in the update
    for i in range(1, len(vals)):
        # if we have rules about this update
        if int(vals[i]) in rules_dict.keys():
            # check if preceding values are in list
            for j in range(0, i):
                if int(vals[j]) in rules_dict[int(vals[i])]:
                    return False
                else:
                    continue
        else:
            continue
    return True

def main():
    file = open('input.txt', 'r')
    text = file.read()

    rules_regex = r"\d+\|\d+"
    rules = re.findall(rules_regex, text)

    update_regex = r".*,.*"
    updates = re.findall(update_regex, text)

    total_val = 0

    corrected_total_val = 0

    rules_dict = {}

    for rule in rules:
        prefix, suffix = rule.split("|")
        if int(prefix) in rules_dict:
            rules_dict[int(prefix)].append(int(suffix))
        else:
            rules_dict[int(prefix)] = []
            rules_dict[int(prefix)].append(int(suffix))

    for update in updates:
        vals = update.split(",")
        valid = check_valid(vals, rules_dict)
        if valid:
            mid_val = vals[(len(vals) // 2)]
            total_val += int(mid_val)

        else: 
            # let's try insertion sort

            corrected_list = [vals[0]]

            # for each element we want to add
            for i in range(1, len(vals)):
                # if there are rules for the element we want to add
                if int(vals[i]) in rules_dict.keys():
                    # check existing values in list
                    for j in range(0, i):
                        # if we have a rule for the element in our corrected list
                        if int(corrected_list[j]) in rules_dict[int(vals[i])]:
                            # insert the new element into the corrected list
                            corrected_list.insert(j, vals[i])
                            break
                    else:
                        # if we get to the end of the list with no conflicts, add it to the end 
                        corrected_list.append(vals[i])

                # if there are no restrictions for this value
                else:
                    corrected_list.append(vals[i])

            mid_val = corrected_list[(len(corrected_list) // 2)]
            corrected_total_val += int(mid_val)

    print("Original total value: " + str(total_val))

    print("Corrected total value: " + str(corrected_total_val))

if __name__ == "__main__":
    main()
