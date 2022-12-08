import numpy as np

filename = "Day5.csv"
overlap =0
count = 0  
dicBox = dict()
newdict = dict()
movesList =list()
listlst = list()
with open(filename) as diary_file:
    c= 1
    for line in diary_file:
        if len(line.strip('\n')) ==0:
            dicBox.pop(c-1)
            print(c)
            listlst.pop()
            continue
        elif line[0:4] == 'move':
            linelst = line.split(" ")
            movesList.append([linelst[1],linelst[3],linelst[5].strip('\n')])
        else:
            count+=1
            linelen =len(line.strip('\n'))
            item = [line[i+1].strip('\n') for i in range(0, len(line), 4)]
            dicBox[c] =item
            listlst.append(item)
            c+=1
    print(dicBox)
    print(listlst)
    listlst = np.array(listlst).T.tolist()

    print(listlst)
    items = c-2
    c=1
    
    for item in listlst:
        newdict[c] = ("".join(item)).strip()
        c+=1
        
    print(newdict)
    for i in movesList:
        num = int(i[0])
        fromI = int(i[1])
        toI=int(i[2])
        itemtomove = newdict[fromI][0:num]
        #itemtomove = itemtomove [::-1]
        newdict[fromI] = newdict[fromI][num:]
        newdict[toI] = itemtomove+newdict[toI]
        print(newdict)
    res = ""
    for (k,v) in newdict.items():
        if len(v)>0:
            res = res+v[0]
        
    print(res)
        

        


   
    