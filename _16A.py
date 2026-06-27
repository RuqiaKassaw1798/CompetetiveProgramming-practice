n, m = map(int, input().split())
p = ''
for i in range(n):
    s = input()
    if len(set(s)) > 1 or s[0] == p:
        print('NO')
        exit()
    p = s[0]
print('YES')
