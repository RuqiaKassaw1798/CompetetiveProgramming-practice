n = int(input())
a = list(map(int, input().split()))

sereja = 0
dima = 0

for i in range(n):
    if a[0] > a[-1]:
        x = a.pop(0)
    else:
        x = a.pop()

    if i % 2 == 0:
        sereja += x
    else:
        dima += x

print(sereja, dima)
