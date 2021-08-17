N=int(input())
for i in range(N):
    k=int(input())
    n=int(input())
    arr1 = [[0 for i in range(n)] for j in range(k+1)] 
    for i in range(k+1):
        for j in range(0,n):
            if i==0:
                arr1[i][j]=j+1
            else :
                for l in range(j+1):
                    arr1[i][j]+=arr1[i-1][l]
                
    print(arr1[k][n-1])
            