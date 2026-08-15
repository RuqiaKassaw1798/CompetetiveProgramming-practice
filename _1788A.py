t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total_twos = a.count(2)

    if total_twos % 2:
        print(-1)
        continue

    half = total_twos // 2
    count = 0

    for i in range(n - 1):
        if a[i] == 2:
            count += 1

        if count == half:
            print(i + 1)
            break
