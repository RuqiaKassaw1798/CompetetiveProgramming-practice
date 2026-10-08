s = input().strip()

letters = set(s)

letters.discard('{')
letters.discard('}')
letters.discard(',')
letters.discard(' ')

print(len(letters))
