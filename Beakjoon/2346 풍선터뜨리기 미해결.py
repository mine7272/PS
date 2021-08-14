from collections import deque

N=int(input())
dq=deque(list(map(int,input().split())))
answer=[]
arr=deque([i for i in range(1,N+1)])


paper=dq.popleft()
answer.append(arr.popleft())

if paper>0:
    while (paper > len(dq)):
        paper-=len(dq)
    answer.append(arr.pop(paper))
    paper=dq.pop(paper)
if paper<0:
    paper*=-1
    while (paper > len(dq)):
        paper-=len(dq)
    
    answer.append(arr.pop(paper))
    paper=dq.pop(paper)