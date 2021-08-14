arr=[]
stack=[]
answer=[]

n=int(input())
j=0
now=1
for i in range(1,n+1):
    num=int(input())
    while now<num:
        arr.append(num)
        answer.append("+")
        now+=1
    
    if stack[-1]==num:
        stack.pop()
        answer.append("-")
    
    if len(arr2)==0:
        break
print("".join(answer))

미완