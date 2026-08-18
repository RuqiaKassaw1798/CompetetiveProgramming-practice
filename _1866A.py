n = int(input())
a = list(map(int, input().split()))

print(min(abs(x) for x in a))
