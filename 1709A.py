t = int(input())
for _ in range(t):
    x = int(input())
    a, b, c = map(int, input().split())
    key_of = {1: a, 2: b, 3: c}
    
    visited = set()
    cur = x
    while cur != 0 and cur not in visited:
        visited.add(cur)
        cur = key_of[cur]
    
    print("YES" if len(visited) == 3 else "NO")
