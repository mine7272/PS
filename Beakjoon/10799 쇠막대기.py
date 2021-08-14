bar_laser=list(input())
answer=0
stack=[]

for i in range(len(bar_laser)):
    if bar_laser[i]=='(':
        stack.append(bar_laser[i])
    else:
        if bar_laser[i-1]=='(':
            stack.pop()
            answer+=stack.count('(')
        else:
            stack.pop()
            answer+=1
print(answer)