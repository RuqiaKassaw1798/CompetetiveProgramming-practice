t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ok = True

    for x in a:
        if x % a[0] != 0:
            ok = False
            break

    print("YES" if ok else "NO")
