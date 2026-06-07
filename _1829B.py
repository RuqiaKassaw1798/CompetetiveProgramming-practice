t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cur = 0
    ans = 0

    for x in a:
        if x == 0:
            cur += 1
            ans = max(ans, cur)
        else:
            cur = 0

    print(ans)
