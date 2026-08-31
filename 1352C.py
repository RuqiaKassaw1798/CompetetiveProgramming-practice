t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    low = 1
    high = n * k

    while low < high:
        mid = (low + high) // 2

        not_divisible = mid - mid // n

        if not_divisible >= k:
            high = mid
        else:
            low = mid + 1

    print(low)
