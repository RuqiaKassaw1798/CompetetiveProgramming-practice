s = input()
i = 0

while i < len(s):
    if s[i] == '.':
        print(0, end='')
        i += 1
    elif s[i:i+2] == '-.':
        print(1, end='')
        i += 2
    else:  # '--'
        print(2, end='')
        i += 2
