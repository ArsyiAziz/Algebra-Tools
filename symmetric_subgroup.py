def symmetric_subgroup(list):
    stop = False
    while not stop:
        #jika ada siklus baru, maka ulangi prosesnya
        stop = True
        for c1 in list:
            for c2 in list:
                temp = dict()
                for i in range(1, 6):
                    #mencari siklus baru
                    temp[i] = c1[c2[i]]
                if temp not in list: 
                    #hanya akan dioutput siklus yang unik
                    list.append(temp)
                    print(f"{c1} ∘ {c2} = {temp}", end="\n--------------\n")
                    stop = False

if __name__ == "__main__":
    cycle1 = {1:1, 2:2, 3:4, 4:5, 5:3} #ini adalah perentang pertama
    cycle2 = {1:1, 2:2, 3:4, 4:3, 5:5} #ini adalah perentang kedua
    list=[cycle1, cycle2]
    symmetric_subgroup(list)
    print("Subgroup: ")
    print(list)
