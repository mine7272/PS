n=int(input())
score=list(map(int,input().split()))
max=0


for i in score:
    if i>max:
        max=i

sum=0
for x in score:
    newscore=float(x/max)*100
    sum+=newscore
print(sum/n)