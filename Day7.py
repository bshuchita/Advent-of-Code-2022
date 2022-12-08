def findmarker(line)->int:
    marker = 1
    seq = ""
    for i in line:
        if i in seq:
            sindex =seq.index(i)
            seq=seq[sindex+1:]
        seq+=i
        if len(seq) == 14:
            break

        marker+=1

    return marker

filename = "Day6.csv"
overlap =0
count = 0  
with open(filename) as diary_file:
    c= 1
    for line in diary_file:
        print(line)
        print(findmarker(line))


   
    