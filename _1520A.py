t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    seen = set()
    ok = True

    for i in range(1, n):
        if s[i] != s[i - 1]:
            seen.add(s[i - 1])
            if s[i] in seen:
                ok = False
                break

    print("YES" if ok else "NO")
