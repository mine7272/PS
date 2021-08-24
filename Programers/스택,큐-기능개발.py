from collections import deque

pr=[40, 93, 30, 55, 60, 65]
sp=[60, 1, 30, 5, 10, 7]
cnt=0
day=deque()
answer = []
for i in range(len(pr)):
    if (100-pr[i])%sp[i]>0:
        day.append(((100-pr[i])//sp[i])+1)
    else:
        day.append((100-pr[i])//sp[i])
gijun=day[0]
while (len(day)>0):
    if len(day)==1:
        cnt+=1
        day.popleft()
        answer.append(cnt)
        break
    elif gijun>=day[1]:
        cnt+=1
        day.popleft()
        continue
    if gijun<day[1]:
        cnt+=1
        day.popleft()
    answer.append(cnt)
    cnt=0
    gijun=day[0]
print(answer)