a=int(input())
b=list(map(int,input()))
answer=0
for i in range(len(b)):
    answer+=b[i]
print(answer)