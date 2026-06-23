n = int(input())
a = list(map(int, input().split()))

odd = sum(x % 2 for x in a)
even = n - odd

if odd == 1:
    print(a.index(next(x for x in a if x % 2 == 1)) + 1)
else:
    print(a.index(next(x for x in a if x % 2 == 0)) + 1)
