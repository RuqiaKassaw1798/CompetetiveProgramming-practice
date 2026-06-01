t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    for x in a:
        if a.count(x) == 1:
            print(a.index(x) + 1)
            break
