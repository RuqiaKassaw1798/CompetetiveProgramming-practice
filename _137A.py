s = input().strip()

ans = 0
cnt = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        cnt += 1
    else:
        ans += (cnt + 4) // 5
        cnt = 1

ans += (cnt + 4) // 5

print(ans)
