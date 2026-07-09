n = int(input())

height = 0
level = 1
need = 0

while True:
    need += level
    if n >= need:
        n -= need
        height += 1
        level += 1
    else:
        break

print(height)
