t = int(input())

for _ in range(t):
    keyboard = input()
    word = input()

    pos = {char: i for i, char in enumerate(keyboard)}

    ans = 0

    for i in range(1, len(word)):
        ans += abs(pos[word[i]] - pos[word[i - 1]])

    print(ans)
