s=input()
u_count=0
l_count=0
for char in s:
    if char.isupper():
        u_count+=1
    else:
        l_count+=1
if u_count<=l_count:
    print(s.lower())
else:
    print(s.upper())
