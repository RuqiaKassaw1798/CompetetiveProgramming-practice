n = int(input())
a = list(map(int, input().split()))

mx = max(a)
ans = sum(mx - x for x in a)

print(ans)
