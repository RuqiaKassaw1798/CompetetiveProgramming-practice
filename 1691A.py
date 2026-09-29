t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    even = sum(x % 2 == 0 for x in a)
    odd = n - even

    print(min(even, odd))
