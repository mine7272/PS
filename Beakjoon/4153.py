while(1):
    a,b,c=map(int,input().split())
    max=a
    if a==0 and b==0 and c==0:
        break
    if max<b and b>c:
        max=b
        if max**2==c**2+a**2:
            print("right")
        else :
            print("wrong")
    elif max<c:
        max=c
        if max**2==a**2+b**2:
            print("right")
        else :
            print("wrong")
    else :
        if max**2==c**2+b**2:
            print("right")
        else :
            print("wrong")