t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    x = 0
    for v in a:
        x ^= v

    if x == 0:
        print(0)
    elif n % 2 == 1:
        print(x)
    else:
        print(-1)
