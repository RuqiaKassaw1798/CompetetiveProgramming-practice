t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    left = 0
    right = 51

    for _ in range(n):
        l, r = map(int, input().split())

        if l <= k <= r:
            left = max(left, l)
            right = min(right, r)

    print("YES" if left == right else "NO")
