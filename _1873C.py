t = int(input())

for i in range(t):
    grid = [input() for i in range(10)]

    ans = 0

    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'X':
                d = min(i, 9 - i, j, 9 - j)
                ans += d + 1

    print(ans)
