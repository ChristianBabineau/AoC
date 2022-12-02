highest=0
moveToNext=False
with open("Day1/input.txt") as f:
    current=0
    for line in f:
        if line =="\n":
            moveToNext=True
        else:
            current=current+int(line)
        if moveToNext:
            if current>highest:
                highest=current
            moveToNext=False
            current=0
print(highest)
        
