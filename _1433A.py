t = int(input())

for i in range(t):
    x = input()
    d = int(x[0])
    l = len(x)
    print((d - 1) * 10 + l * (l + 1) // 2)
