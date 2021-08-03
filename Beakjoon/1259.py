while True:
    s=1
    a=input()
    if a=="0":
        break
    a=list(a)
    for i in range(len(a)//2):
        if a[i]!=a[len(a)-1-i]:
            s=0
            break
    if s==0:print("no")
    else : print("yes")