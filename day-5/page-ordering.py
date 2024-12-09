import re

def main():
    file = open('input.txt', 'r')
    text = file.read()

    rules_regex = r"\d+\|\d+"
    rules = re.findall(rules_regex, text)

    update_regex = r".*,.*"
    updates = re.findall(update_regex, text)

    total_val = 0

    rules_dict = {}

    for rule in rules:
        prefix, suffix = rule.split("|")
        if int(prefix) in rules_dict:
            rules_dict[int(prefix)].append(int(suffix))
        else:
            rules_dict[int(prefix)] = []
            rules_dict[int(prefix)].append(int(suffix))

    for update in updates:
        valid = True
        vals = update.split(",")
        # iterate through each value in the update
        for i in range(1, len(vals)):
            if valid:
                # if we have rules about this update
                if int(vals[i]) in rules_dict.keys():
                    # check if preceding value is in list
                    if int(vals[i-1]) in rules_dict[int(vals[i])]:
                        valid = False
                    else:
                        continue
                else:
                    continue
            else:
                break
        if valid:
            mid_val = vals[(len(vals) // 2)]
            total_val += int(mid_val)

        else: 
            continue

    print(total_val)
        

if __name__ == "__main__":
    main()
