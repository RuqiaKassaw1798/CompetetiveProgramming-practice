t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    if a[0] == a[-1]:
        print(-1)
        continue

    mn = a[0]
    b = []
    c = []

    for x in a:
        if x == mn:
            b.append(x)
        else:
            c.append(x)

    print(len(b), len(c))
    print(*b)
    print(*c)
