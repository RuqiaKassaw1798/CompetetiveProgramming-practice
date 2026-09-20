t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    c = min(s)
    i = s.rfind(c)

    print(c + s[:i] + s[i + 1:])
