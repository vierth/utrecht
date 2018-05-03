t1 = open("shilengths.txt","r").read().split("\n")
t2 = open("weilengths.txt","r").read().split("\n")
my_dict = {}
for line in t1:
    info = line.split("\t")
    if info[0] in my_dict:
        my_dict[info[0]].append("S")
    else:
        my_dict[info[0]] = ["S"]

for line in t2:
    info = line.split("\t")
    if info[0] in my_dict:
        my_dict[info[0]].append("W")
    else:
        my_dict[info[0]] = ["W"]

jsvar = "var weiandshidocs = ["

save = []

for key in my_dict.keys():
    label = my_dict[key]
    if len(label) == 2:
        label = "B"
    else:
        label = label[0]
    save.append("{"+f"doc:\"{key}\",label:\"{label}\""+ "}")

jsvar1 = jsvar + ",".join(save) + "]"

t1 = open("shimentions.txt","r").read().split("\n")
t2 = open("weimentions.txt","r").read().split("\n")

mention_dict = {}

for line in t1:
    info = line.split("\t")
    if info[0] in mention_dict:
        mention_dict[info[0]].append("S")
    else:
        mention_dict[info[0]] = ["S"]
for line in t2:
    info = line.split("\t")
    if info[0] in mention_dict:
        mention_dict[info[0]].append("W")
    else:
        mention_dict[info[0]] = ["W"]

jsvar = "var mentions = ["

save = []

for key in mention_dict.keys():
    label = mention_dict[key]
    if len(label) == 2:
        label = "B"
    else:
        label = label[0]
    save.append("{"+f"doc:\"{key}\",label:\"{label}\""+ "}")

jsvar2 = jsvar + ",".join(save) + "]"



wf = open("weiandshiinfo.js", "w")
wf.write(jsvar1+"\n")
wf.write(jsvar2)
wf.close()