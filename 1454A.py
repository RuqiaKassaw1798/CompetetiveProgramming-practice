t = int(input())

for _ in range(t):
    n = int(input())
    a = list(range(1, n + 1))

    a = a[1:] + a[:1]

    print(*a)
