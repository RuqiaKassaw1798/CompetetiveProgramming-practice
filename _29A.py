n = int(input())
camels = []

for i in range(n):
    x, d = map(int, input().split())
    camels.append((x, d))

for i in range(n):
    for j in range(i + 1, n):
        if camels[i][0] + camels[i][1] == camels[j][0] and \
           camels[j][0] + camels[j][1] == camels[i][0]:
            print("YES")
            exit()

print("NO")
