t = int(input())

for _ in range(t):
    n = int(input())

    best_sum = 0
    answer = 2

    for x in range(2, n + 1):
        s = sum(range(x, n + 1, x))

        if s > best_sum:
            best_sum = s
            answer = x

    print(answer)
