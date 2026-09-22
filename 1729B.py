t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = []

    i = n - 1
    while i >= 0:
        if s[i] == '0':
            x = int(s[i - 2:i])
            i -= 3
        else:
            x = int(s[i])
            i -= 1

        ans.append(chr(96 + x))

    print("".join(ans[::-1]))
