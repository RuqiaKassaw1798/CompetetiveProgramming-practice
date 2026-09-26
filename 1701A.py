t = int(input())

for _ in range(t):
    a = input()
    b = input()

    ones = a.count("1") + b.count("1")

    if ones == 0:
        print(0)
    elif ones == 4:
        print(2)
    else:
        print(1)
