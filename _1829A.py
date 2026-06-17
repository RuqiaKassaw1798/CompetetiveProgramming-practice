t = int(input())
target = "codeforces"

for _ in range(t):
    s = input().strip()
    cnt = 0

    for i in range(10):
        if s[i] != target[i]:
            cnt += 1

    print(cnt)
