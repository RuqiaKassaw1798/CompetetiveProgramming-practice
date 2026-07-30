n = int(input())
a = list(map(int, input().split()))

total = sum(abs(x) for x in a)
neg = sum(1 for x in a if x < 0)
mn = min(abs(x) for x in a)

if n % 2 == 1 or neg % 2 == 0:
    print(total)
else:
    print(total - 2 * mn)
