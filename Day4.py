filename = "Day4.csv"
overlap =0
count = 0  
with open(filename) as diary_file:
    for line in diary_file:
        count+=1
        line =  line.rstrip().split(sep = ',')
        x1,y1 = line[0].split(sep="-")
        x2,y2 = line[1].split(sep="-")

        x1=int(x1)
        x2=int(x2)
        y1=int(y1)
        y2=int(y2)
        
        print(x1,y1)
        print(x2,y2)
        z1 =y1-x1
        z2 =y2-x2
        """
        5-7,7-9 overlaps in a single section, 7.
        2-8,3-7 overlaps all of the sections 3 through 7.
        6-6,4-6 overlaps in a single section, 6.
        2-6,4-8 overlaps in sections 4, 5, and 6.
        if(z1<z2):
            if(y1<=y2 and x1>=x2):
                overlap+=1
        elif (z2<z1):
            if(y2<=y1 and x2>=x1):
                overlap+=1
        else:
            if(y2==y1 and x2==x1):
                overlap+=1
        """
        if(x1<=x2 and y1>=x2 and y1 <=y2):
            overlap+=1
        elif(x1<=x2 and y1>=x2 and y1 >=y2):
            overlap+=1
        elif(x2<=x1 and y2>=x1 and y2 <=y1):
            overlap+=1
        elif(x2<=x1 and y2>=x1 and y2 >=y1):
            overlap+=1
        
    print(count,overlap,count-overlap)    
    """
        l = int((len(line))/2)
        firstH = line[0:l]
        secondH = line[l:]
        res = set(firstH).intersection(secondH)
        if len(res)>0:
            for x in res:
                if x.islower() == False: # upper case
                    score+=alph[x.lower()]+26
                else:
                    score+=alph[x]
                
        print(line,len(firstH) ,len(secondH), firstH, secondH)
        print("common : ", res)
        """
   
    