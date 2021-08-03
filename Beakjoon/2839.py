N=int(input())

a=N//5
NN=N%5
b=NN//3
while a>=0:
    if NN%3!=0:
        a-=1
        NN=N-(a*5)
        b=NN//3
    elif NN%3==0:
        print(a+b)
        break
if a<0:print(-1)