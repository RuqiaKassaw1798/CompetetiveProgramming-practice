n,h=map(int,input().split())
a=list(map(int,input().split()))
count=0
for c in a:
    if c<=h:
        count+=1
    else:
        count+=2
print(count)
