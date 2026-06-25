n = int(input())
a = list(map(int, input().split()))

print(max(a.count(x) for x in a), len(set(a)))
