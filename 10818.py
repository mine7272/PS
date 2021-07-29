a=int(input())
b=list(map(int,input().split()))

min=b[0]
max=b[0]
for i in range(1,a):
    if b[i]>max:max=b[i]
    if b[i]<min:min=b[i]

print("%d %d"%(min,max))