a=int(input())
for i in range(a):
    score=0
    endscore=0
    b=list(input())
    for j in range(len(b)):
        if b[j]=="O":
            score+=1
            endscore+=score
        if b[j]=="X":
            score=0
    print(endscore)