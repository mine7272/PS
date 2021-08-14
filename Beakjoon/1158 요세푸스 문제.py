N,K=map(int,input().split())
a=[i for i in range(1,N+1)]
answer=[]
out=K-1

for i in range(N):
    if len(a)>out:
        answer.append(a.pop(out))
        out+=K-1
    elif len(a)<=out:
        out=out%len(a)
        answer.append(a.pop(out))
        out+=K-1

    
print("<", ", ".join(str(i) for i in answer), ">", sep='')