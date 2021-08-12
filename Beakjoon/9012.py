T=int(input())
stack=[]
for _ in range(T):
    vps=list(input())
    j=0
    for i in range(len(vps)):
        if vps[i]=='(' :
            stack.append(vps[i])
            j+=1
        elif stack[j-1]=='(':
            stack.pop()
            j-=1
            if i==len(vps)-1:
                print("yes")
                break
        else :
            print("No")
            break