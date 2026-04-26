n = int(input())
x = int(input())
possible = True
for _ in range(n):
    a, b = map(int, input().split())
    if a == x or a == 7 - x or b == x or b == 7 - x:
        possible = False
if possible:
    print("YES")
else:
    print("NO")
