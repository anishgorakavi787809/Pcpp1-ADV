import csv


arr = []
with open("lol.csv","r") as l:
    vs = csv.reader(l)

    for v in vs:
        category = v.pop()
        for s in v:
            #print([s,category])
            arr.append([s,category])

s = open("graph.csv","w")

ss = csv.writer(s)

ss.writerows(arr)