word=input().upper()
wordlist=list(set(word))#집합자료형이지만 중복요소를 거르는데에도 사용함
cnt=[]
max=0

for i in wordlist:
    count=word.count(i)#count를 몰라서 풀기 어려웠음
    if count==max:
        maxword='?'
    if count>max: #두개의 if문 위치를 바꾸면 틀림. :틀린이유
        max=count
        maxword=i 

print(maxword)