N,M=map(int,input().split())
arr1=list(map(int,input().split()))

min=300000
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            sum=arr1[i]+arr1[j]+arr1[k]
            if M>=sum:   
                if M-sum<min:
                    min=M-sum
                    answer=sum
print(answer)