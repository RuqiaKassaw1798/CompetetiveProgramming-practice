t = int(input())

for i in range(t):
    ans = ""

    for i in range(8):
        s = input()
        for c in s:
            if c != ".":
                ans += c

    print(ans)
