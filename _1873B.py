t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    a[0] += 1

    ans = 1
    for x in a:
        ans *= x

    print(ans)
