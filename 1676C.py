t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]

    ans = 10**9

    for i in range(n):
        for j in range(i + 1, n):
            diff = 0

            for k in range(m):
                diff += abs(ord(s[i][k]) - ord(s[j][k]))

            ans = min(ans, diff)

    print(ans)
