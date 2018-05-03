import pickle
import numpy as np
import time

matchscore = 1
misalignscore = -1
mismatchscore = -1

df = open("edgesnc.js","r")
info = df.read()
df.close()

lines= info.split("\n")
sl = []
for line in lines:
    texts = []
    if "firstquote:" in line:
        beginning = line[:line.find("firstquote:\"")+12]
        
        line = line[line.find("firstquote:\"")+12:]
        quote1 = line[:line.find("\"")]
        line = line[line.find("secondquote:\"")+13:]
        quote2 = line[:line.find("\"")]
        end = line[line.find("\""):]

        texts = [quote1, quote2]
        






        matrix = np.zeros([len(texts[0])+1,len(texts[1])+1])

      

        # prep matrix:
        for j in range(len(texts[1])+1):
            matrix[0][j] = -j

        for i in range(len(texts[0])+1):
            matrix[i][0] = -i

        s = time.time()
        for i in range(len(texts[0])):
            for j in range(len(texts[1])):
                c1 = texts[0][i]
                c2 = texts[1][j]

                if c1 == c2:
                    score = matchscore
                else:
                    score = mismatchscore

                matrixrow = i+1
                matrixcolumn = j+1

                upperscore = matrix[i][j+1] + misalignscore
                leftscore = matrix[i+1][j] + misalignscore
                diagnal = matrix[i][j] + score

                currentscore = max([upperscore, leftscore, diagnal])

                matrix[matrixrow][matrixcolumn] = currentscore

        stringa = ""
        stringb = ""

        #traceback
        i = len(matrix)-1
        j = len(matrix[0])-1

        finalscore = matrix[i][j]

        while i > 0 or j > 0:
            upper = matrix[i][j - 1]
            left  = matrix[i-1][j]
            diag = matrix[i-1][j-1]
            maxval = max([upper, left, diag]) 
            if maxval == diag:
                i -= 1
                j -= 1
                stringa = texts[0][i] + stringa
                stringb = texts[1][j] + stringb
            elif maxval == upper:
                j -= 1
                stringa = " "+stringa
                stringb = texts[1][j] + stringb
            elif maxval == left:
                i -= 1
                stringa = texts[0][i] + stringa
                stringb = " "+stringb
            
        while stringa[-1] == " " or stringb[-1] == " " or stringa[-1] != stringb[-1]:
            stringa = stringa[:-1]
            stringb = stringb[:-1]
        

        savesring = beginning + stringa + "\",secondquote:\""+stringb + end
        print(savesring)
        sl.append(savesring)
    else:
        sl.append(line)

wf = open("edgesaligned.js", "w")
wf.write("\n".join(sl))
wf.close()