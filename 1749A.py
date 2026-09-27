t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    for _ in range(m):
        input()

    print("YES" if m < n else "NO")
