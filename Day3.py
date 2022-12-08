filename = "Day3.csv"
elveC =list()
alph = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26
}
with open(filename) as diary_file:
    score = 0
    lines = list()
    for line in diary_file:
        line =  line.rstrip()
        lines.append(line)
    
    count = 0
    resLast = ""
    for x in lines:
        if count==0:
            resLast = x
        elif count<3:
            resLast = set(x).intersection(resLast)
        count+=1
        if(count==3):
            count=0
            if len(resLast)>0:
                for y in resLast:
                    if y.islower() == False: # upper case
                        score+=alph[y.lower()]+26
                    else:
                        score+=alph[y]

    print(score)    
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
    print(score)

    