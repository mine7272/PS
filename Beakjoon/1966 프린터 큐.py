from collections import deque

def getmax():
    max=0
    for i in range(len(que)):
        if que[i]>max:
            max=que[i]
    return max

T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    que=deque(list(map(int,input().split())))
    cnt=0
    max=getmax()
    while(1):
        if que[0]<max:
            if M-1<0:
                M=len(que)-1
            else:
                M-=1
            que.append(que.popleft())
        else : 
            que.popleft()
            cnt+=1
            if M==0:
                print(cnt)
                break
            M-=1
            max=getmax()