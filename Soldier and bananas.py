k, n, w = map(int, input().split())
t=0
for i in range(1,w+1):
    t+=i*k
x=t-n
print(max(0, x))
