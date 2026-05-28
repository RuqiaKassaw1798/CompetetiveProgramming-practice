n=int(input())
for i in range(n):
     a,b,c=map(int, input().split())
     if c==a+b:
          print("+")
     else:
          print("-")
