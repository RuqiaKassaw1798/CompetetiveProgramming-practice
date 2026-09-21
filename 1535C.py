t = int(input())

for _ in range(t):
    s = input()
    dp0 = dp1 = 0
    ans = 0

    for c in s:
        old0, old1 = dp0, dp1

        if c != '1':
            dp0 = old1 + 1
        else:
            dp0 = 0

        if c != '0':
            dp1 = old0 + 1
        else:
            dp1 = 0

        ans += max(dp0, dp1)

    print(ans)
