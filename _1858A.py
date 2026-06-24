t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())

    first = a + (c + 1) // 2
    second = b + c // 2

    if first > second:
        print("First")
    else:
        print("Second")
