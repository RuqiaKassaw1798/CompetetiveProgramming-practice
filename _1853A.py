t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ok = False
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            ok = True
            break

    if ok:
        print(0)
    else:
        mn = float('inf')
        for i in range(n - 1):
            mn = min(mn, a[i + 1] - a[i])
        print(mn // 2 + 1)
