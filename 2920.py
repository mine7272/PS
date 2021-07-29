a=list(input().split())
s=0
if a[0]=="1":
    s=1
    for i in range(8):
        if a[i]!=str(i+1):
            s=0
            break
elif a[0]=="8":
    s=2
    for i in range(8):
        if a[i]!=str(8-i):
            s=0
            break
if s==0 : print("mixed")
elif s==1 : print("ascending")
elif s==2 : print("descending")
