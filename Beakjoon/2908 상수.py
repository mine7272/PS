a,b=input().split()
a=list(a)
a.reverse()
b=list(b)
b.reverse()

a="".join(a)
b="".join(b)

a=int(a)
b=int(b)

if a>b:
    print(a)
else : print(b)