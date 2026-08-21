n, m = map(int, input().split())

colored = False

for _ in range(n):
    pixels = input().split()
    for p in pixels:
        if p in {'C', 'M', 'Y'}:
            colored = True

print("#Color" if colored else "#Black&White")
