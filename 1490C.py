t = int(input())

for _ in range(t):
    x = int(input())
    ok = False

    for a in range(1, 10000):
        if a ** 3 >= x:
            break

        b = round((x - a ** 3) ** (1 / 3))

        if b ** 3 == x - a ** 3:
            ok = True
            break

    print("YES" if ok else "NO")
