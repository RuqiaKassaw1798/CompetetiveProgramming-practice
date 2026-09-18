t = int(input())

for _ in range(t):
    n = int(input())
    s = input().lower()

    ans = ""

    for c in s:
        if not ans or ans[-1] != c:
            ans += c

    print("YES" if ans == "meow" else "NO")
