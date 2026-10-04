t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    upper = [0] * 26
    lower = [0] * 26

    for c in s:
        if c.isupper():
            upper[ord(c) - 65] += 1
        else:
            lower[ord(c) - 97] += 1

    ans = 0

    for i in range(26):
        pairs = min(upper[i], lower[i])
        ans += pairs

        upper[i] -= pairs
        lower[i] -= pairs

        extra = max(upper[i], lower[i]) // 2
        use = min(k, extra)

        ans += use
        k -= use

    print(ans)
