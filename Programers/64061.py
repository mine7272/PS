def solution(board, moves):
    baguny=[]
    lastbaguny=0
    cnt=0
    for i in range(len(moves)):
        a=moves[i]-1
        b=0
        try:
            while board[b][a]==0:
                b=b+1
        except:
                break
        if len(baguny)>0:
            lastbaguny=baguny[-1]
        baguny.append(board[b][a])
        board[b][a]=0
        if lastbaguny==baguny[-1]:
            cnt+=2
            baguny.pop()
            baguny.pop()
    return cnt