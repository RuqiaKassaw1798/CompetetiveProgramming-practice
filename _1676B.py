t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mn = min(a)
    ans = 0

    for x in a:
        ans += x - mn

    print(ans)
