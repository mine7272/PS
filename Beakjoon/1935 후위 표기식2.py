n=int(input())
susik=input()
stack=[]
arr=[]

for i in range(n):
    arr.append(int(input()))

for i in susik:
    if 'A'<= i <='Z':
        stack.append(arr[ord(i)-ord('A')])
    
    else:
        a=stack.pop()
        b=stack.pop()
        if  i=='*':
            stack.append(b*a)
        if  i=='/':
            stack.append(b/a)
        if  i=='+':
            stack.append(b+a)
        if  i=='-':
            stack.append(b-a)
print("%.2f" %stack[0])