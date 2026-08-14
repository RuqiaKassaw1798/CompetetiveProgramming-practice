t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    side = max(max(a, b), 2 * min(a, b))
    print(side * side)
