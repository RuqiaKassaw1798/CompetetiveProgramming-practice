t = int(input())

for i in range(t):
    a = list(map(int, input().split()))
    if a.count(a[0]) == 4:
        print("YES")
    else:
        print("NO")
