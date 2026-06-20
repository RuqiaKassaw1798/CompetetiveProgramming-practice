t = int(input())

for i in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    print(max(h) - min(h) + 1)
