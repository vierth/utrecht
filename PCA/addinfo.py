alldata = open("pointdatascaled.tsv","r").read().split("\n")

t1 = open("shilengths.txt","r").read().split("\n")
t2 = open("weilengths.txt","r").read().split("\n")
t3 = open("shimentions.txt","r").read().split("\n")
t4 = open("weimentions.txt","r").read().split("\n")

addedlabels = {}

for l in t1:
    info = l.split("\t")
    if info[0] not in addedlabels:
        addedlabels[info[0]] = ["S","N"]

for l in t2:
    info = l.split("\t")
    if info[0] not in addedlabels:
        addedlabels[info[0]] = ["W","N"]
    else:
        addedlabels[info[0]] = ["B", "N"]

for l in t3:
    info = l.split("\t")
    addedlabels[info[0]][1] = "S"

for l in t4:
    info = l.split("\t")
    if addedlabels[info[0]][1] == "S":
        addedlabels[info[0]][1] = "B"
    else:
        addedlabels[info[0]][1] = "W"

save = [alldata[0]+"\tWorkContains\tDocumentContains"]

for i in range(1,len(alldata)):
    line = alldata[i]
    info = line.split("\t")
    key = info[10]+"_"+info[5]
    try:
        mentions = addedlabels[key]
        save.append(alldata[i]+"\t"+mentions[0]+"\t"+mentions[1])
    except:
        save.append(alldata[i]+"\tN\tN")

wf = open('addedvalue.tsv',"w")
wf.write("\n".join(save))
wf.close()