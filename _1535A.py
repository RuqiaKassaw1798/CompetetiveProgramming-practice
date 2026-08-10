t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))

    finalists = [max(a[0], a[1]), max(a[2], a[3])]
    strongest = sorted(a)[-2:]

    if sorted(finalists) == strongest:
        print("YES")
    else:
        print("NO")
