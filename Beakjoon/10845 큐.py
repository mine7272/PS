import sys

cmdnum=int(sys.stdin.readline())
queue=[]
for _ in range(cmdnum):
    a=sys.stdin.readline().split()
   
    if a[0]=='push':
        queue.append(a[1])
    if a[0]=='pop':
        if len(queue)==0:
            print(-1)
        else: print(queue.pop(0))
    if a[0]=='size':
        print(len(queue))
    if a[0]=='empty':
        if len(queue)==0:
            print(1)
        else: print(0)
    if a[0]=='front':
        if len(queue)==0:
            print(-1)
        else:print(queue[0])
    if a[0]=='back':
        if len(queue)==0:
            print(-1)
        else:print(queue[-1])