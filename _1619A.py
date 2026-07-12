t = int(input())

for i in range(t):
    s = input()

    if len(s) % 2 == 1:
        print("NO")
    else:
        mid = len(s) // 2
        if s[:mid] == s[mid:]:
            print("YES")
        else:
            print("NO")
