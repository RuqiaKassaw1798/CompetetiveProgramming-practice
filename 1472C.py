t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0] * n

    for i in range(n - 1, -1, -1):
        j = i + a[i]

        dp[i] = a[i]

        if j < n:
            dp[i] += dp[j]

    print(max(dp))
