def symmetric_subgroup(list):
    count = 0
    stop = False
    while not stop:
        stop = True
        for c1 in list:
            for c2 in list:
                temp = dict()
                for i in range(1, 6):
                    temp[i] = c1[c2[i]]
                count += 1
                if temp not in list:
                    list.append(temp)
                    print(f"{c1} . {c2} = {temp}", end="\n--------------\n")
                    stop = False
    print(count)

if __name__ == "__main__":
    print("working")
    cycle1 = {1:1, 2:2, 3:4, 4:5, 5:3}
    cycle2 = {1:1, 2:2, 3:4, 4:3, 5:5}
    list=[cycle1, cycle2]
    symmetric_subgroup(list)
    print(len(list))
    print(list)
