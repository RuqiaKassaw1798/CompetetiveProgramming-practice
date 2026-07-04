t = int(input())

for i in range(t):
    n = int(input())

    if n % 4 != 0:
        print("NO")
        continue

    print("YES")

    arr = []
    even_sum = 0
    for i in range(1, n // 2 + 1):
        arr.append(2 * i)
        even_sum += 2 * i
    odd_sum = 0
    for i in range(1, n // 2):
        arr.append(2 * i - 1)
        odd_sum += 2 * i - 1
    arr.append(even_sum - odd_sum)

    print(*arr)
