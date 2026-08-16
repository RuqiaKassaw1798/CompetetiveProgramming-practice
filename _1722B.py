t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()

    possible = True

    for i in range(n):
        if a[i] == 'R' or b[i] == 'R':
            if a[i] != b[i]:
                possible = False
                break

    print("YES" if possible else "NO")
