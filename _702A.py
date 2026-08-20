n = int(input())
a = list(map(int, input().split()))

current = 1
answer = 1

for i in range(1, n):
    if a[i] > a[i - 1]:
        current += 1
    else:
        current = 1

    answer = max(answer, current)

print(answer)
