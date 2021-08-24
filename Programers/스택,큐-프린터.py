from collections import deque
def getmax(dq):
    max=0
    for i in range(len(dq)):
        if dq[i]>max:
            max=dq[i]
    return max

def solution(pr, lo):
    answer = 0
    dq=deque(pr)
    cnt=0
    maxx=getmax(dq)
    while len(dq)>0:
        if dq[0]==maxx:
            dq.popleft()
            cnt+=1
            maxx=getmax(dq)
            if lo==0:
                return cnt
            lo-=1
        else :
            dq.append(dq.popleft())
            lo-=1
            if lo<0:
                lo=len(dq)-1

print(solution([1, 1, 9, 1, 1, 1],0))