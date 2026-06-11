t = int(input())

for _ in range(t):
    k = int(input())

    cnt = 0
    num = 1

    while True:
        if num % 3 != 0 and num % 10 != 3:
            cnt += 1
            if cnt == k:
                print(num)
                break

        num += 1
