a=int(input())
b=int(input())
c=int(input())
gop=a*b*c
gop=list(str(gop))

conunt=[]
for i in range(0,10):
    count=gop.count(str(i))
    print(count)
