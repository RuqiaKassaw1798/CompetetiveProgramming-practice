t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    x = input().strip()
    s = input().strip()

    for ops in range(6):
        if s in x:
            print(ops)
            break
        x += x
    else:
        print(-1)
