t = int(input())

for _ in range(t):
    n = int(input())
    print("NO" if n & (n - 1) == 0 else "YES")
