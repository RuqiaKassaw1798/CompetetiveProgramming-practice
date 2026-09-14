t = int(input())
for i in range(t):
    s = input()
    ans = 0
    for i in range(10):
        if s[i] != "codeforces"[i]:
            ans += 1
    print(ans)
