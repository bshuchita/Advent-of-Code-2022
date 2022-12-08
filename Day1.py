filename = "Day1.csv"
elveC =list()
with open(filename) as diary_file:
    elfCount = 1
    calcount = 0
    for line in diary_file:
        #print(line)
        if line == '\n': 
            elveC.append(calcount)        
            calcount = 0
            continue
        calcount +=int(line)
    elveC.append(calcount)  
print(elveC)
elveC.sort(reverse=True)
print(elveC)
print(elveC[0:4])
#print(max(elveC))
print(sum(elveC[0:3]))
