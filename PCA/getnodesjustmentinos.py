f = open("addedvalue.tsv").read().split("\n")
savenodes = []
for i in range(1,len(f)):
    line = f[i]
    info = line.split("\t")
    if info[-1] != "N":
        savenodes.append(info[10]+"_"+info[5])
print(savenodes)

of = open("edgeswsmentions.txt","r").read().split("\n")
saveedges = []
formated = []
for line in of:
    info = line.split("\t")
    if info[0] in savenodes and info[1] in savenodes:
        saveedges.append(line)
        formated.append("{source: \""+f"{info[0]}\",target:\"{info[1]}\",value:{info[2]}"+"}")

print(formated)

wf=open('limitededgesW.txt','w')
wf.write("\n".join(saveedges))
wf.close()

wf= open("networkdataW.js","w")
wf.write("var networkDataW = ["+",".join(formated)+"]")
wf.close()