score=0
with open("Day2/input.txt") as f:
    for line in f:
        opp=line[0]
        me=line[2]
        if me=='X':
            score=score+1
            if opp=='C':
                score=score+6
            elif opp=='A':
                score=score+3       
        elif me=='Y':
            score=score+2
            if opp=='A':
                score=score+6
            elif opp=='B':
                score=score+3  
        else:
            score=score+3
            if opp=='B':
                score=score+6
            elif opp=='C':
                score=score+3 
print(score)