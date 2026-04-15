n = int(input())
while True:
    n += 1
    s = str(n)
    if len(set(s)) == len(s):
        print(n)
        break
