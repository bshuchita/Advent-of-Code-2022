filename = "Day2.csv"
elveC =list()
with open(filename) as diary_file:
    elfCount = 1
    calcount = 0
    score = 0
    for line in diary_file:
        line =  line.rstrip().split(sep=" ")
        print(line)
        if line[1] == 'X' : #lost
            if line[0] == 'A':
                line[1] = 'Z'
            elif line[0] == 'B':
                line[1] = 'X'
            elif line[0] == 'C':
                line[1] = 'Y'
        elif line[1] == 'Z' : #win
            if line[0] == 'A':
                line[1] = 'Y'
            elif line[0] == 'B':
                line[1] = 'Z'
            elif line[0] == 'C':
                line[1] = 'X'
        elif line[1] == 'Y' : #draw
            if line[0] == 'A':
                line[1] = 'X'
            elif line[0] == 'B':
                line[1] = 'Y'
            elif line[0] == 'C':
                line[1] = 'Z'


        if (line[1] == 'X' and line[0] == 'C') or (line[1] == 'Z' and line[0] == 'B') or (line[1] == 'Y' and line[0] == 'A'):
            score +=6
        elif (line[1] == 'X' and line[0] == 'A') or (line[1] == 'Z' and line[0] == 'C') or (line[1] == 'Y' and line[0] == 'B'):
            score +=3
        
        

        match line[1]:
            case 'X':
                score +=1
            case 'Y':
                score +=2
            case 'Z':
                score +=3
            
    print(score)
