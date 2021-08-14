x,y,w,h=map(int,input().split())
answer=x
if answer >y:answer=y
if answer >h-y:answer=h-y
if answer >w-x:answer=w-x
print(answer)