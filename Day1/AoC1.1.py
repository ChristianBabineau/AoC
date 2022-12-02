highest=0
second=0
third=0
moveToNext=False
with open("Day1/input.txt") as f:
    current=0
    for line in f:
        if line =="\n":
            moveToNext=True
        else:
            current=current+int(line)
        if moveToNext:
            if current>third:
                if current>second:
                    if current>highest:
                        third=second
                        second=highest
                        highest=current
                    else:
                        third=second
                        second=current
                else:
                    third=current
            moveToNext=False
            current=0
print(highest+second+third)
        
