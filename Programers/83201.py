s=[[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]
ss=[]
answer=[]
for i in range(len(s)):
    score=0
    sw=0
    smin=s[i][i]
    smax=s[i][i]
    for j in range(len(s)):
        if j!=i and ((smin==s[j][i] and s[j][i]==s[i][i]) or (smax==s[j][i] and s[j][i]==s[i][i])):
            sw=1        
        if smin>s[j][i]:
            smin=s[j][i]
        if s[j][i]>smax:
            smax=s[j][i]
        score+=s[j][i]
    
    if sw==0 and (smin==s[i][i] or smax==s[i][i]):
        score-=s[i][i]
        score=score/(len(s)-1)
    else: score=score/len(s)
    ss.append(score)
for k in ss:
    if k>=90:
        answer.append("A")
    elif k>=80:
        answer.append("B")
    elif k>=70:
        answer.append("C")
    elif k>=50:
        answer.append("D")
    else :
        answer.append("F")    
print("".join(answer))