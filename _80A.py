n, m = map(int, input().split())

def prime(x):
    return all(x % i for i in range(2, int(x**0.5) + 1))

x = n + 1
while not prime(x):
    x += 1

print("YES" if x == m else "NO")
