t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))
    small, big = a[:n], a[n:]
    res = []
    for s, b in zip(small, big):
        res.append(s)
        res.append(b)
    print(*res)
