t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ones = a.count(1)
    twos = a.count(2)

    total = ones + 2 * twos

    if total % 2:
        print("NO")
    elif ones == 0 and twos % 2:
        print("NO")
    else:
        print("YES")
