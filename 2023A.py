t = int(input())

for _ in range(t):
    n = int(input())
    a = []

    for _ in range(n):
        x, y = map(int, input().split())
        a.append((min(x, y), max(x, y), x, y))

    a.sort()

    ans = []
    for _, _, x, y in a:
        ans += [x, y]

    print(*ans)
