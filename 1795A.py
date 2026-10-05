t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = input()
    b = input()

    s = a + b[::-1]

    bad = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            bad += 1

    print("YES" if bad <= 1 else "NO")
