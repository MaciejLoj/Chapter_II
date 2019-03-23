def duplicates():
    with open('Exercise_1.txt', newline='') as inputfile:
        valid = []
        invalid = []
        cont = inputfile.readlines()
        cont = [x.strip() for x in cont]
        for i in cont:
            divided = i.split()
            clean_list = []
            for i in divided:
                if i not in clean_list:
                    clean_list.append(i)
                else:
                    pass
            if clean_list == divided:
                valid.append(divided)
            else:
                invalid.append(divided)
    print(len(valid), "skyphrases are valid")


duplicates()
