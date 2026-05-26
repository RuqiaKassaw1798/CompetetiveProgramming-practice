a, b = map(int, input().split())

diff = min(a, b)
same = abs(a - b) // 2

print(diff, same)
