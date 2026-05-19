n, k = map(int, input().split())

time_left = 240 - k
solved = 0

for i in range(1, n + 1):
    if time_left >= 5 * i:
        time_left -= 5 * i
        solved += 1
    else:
        break

print(solved)
