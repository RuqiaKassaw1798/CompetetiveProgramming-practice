t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()

    a = a.replace("G", "B")
    b = b.replace("G", "B")

    print("YES" if a == b else "NO")
