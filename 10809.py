alp=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
word=list(input())
for i in range(len(alp)):
    for j in range(len(word)):
        if word[j]==alp[i]:
            alp[i]=j
    if type(alp[i])==str:
        alp[i]=-1
    print(alp[i],end=" ")