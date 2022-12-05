score=0
with open("Day2/input.txt") as f:
    for line in f:
        opp=line[0]
        me=line[2]
        #A=Rock 1  B=Paper 2  C=Scissors 3
        #X=lose Y=draw Z=win
        if me =='X':
            if opp=='A':
                score = score+3
            elif opp=='B':
                score=score+1
            else:
                score=score+2
        elif me=='Y':
            if opp=='A':
                score=score+1+3
            elif opp=='B':
                score=score+2+3
            else:
                score=score+3+3
        else:
            if opp=='A':
                score = score+2+6
            elif opp=='B':
                score=score+3+6
            else:
                score=score+1+6
print(score)