grid = [input() for _ in range(3)]

ok = True
for i in range(3):
    for j in range(3):
        if grid[i][j] != grid[2 - i][2 - j]:
            ok = False

print("YES" if ok else "NO")
