t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    a = b = 0

    for i in range(n):
        if arr[i] % 2 != i % 2:
            if i % 2 == 0:
                a += 1
            else:
                b += 1

    print(a if a == b else -1)
