n = int(input())
a = sorted(map(int, input().split()), reverse=True)

total = sum(a)
s = 0

for i, x in enumerate(a):
    s += x
    if s > total - s:
        print(i + 1)
        break
