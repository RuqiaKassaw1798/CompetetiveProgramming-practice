t = int(input())

for i in range(t):
    s = input()

    ans = s[0]
    for i in range(1, len(s), 2):
        ans += s[i]

    print(ans)
