t = int(input())

for _ in range(t):
    n = int(input())

    players = [input().split() for _ in range(3)]

    count = {}

    for words in players:
        for word in words:
            count[word] = count.get(word, 0) + 1

    scores = []

    for words in players:
        score = 0

        for word in words:
            if count[word] == 1:
                score += 3
            elif count[word] == 2:
                score += 1

        scores.append(score)

    print(*scores)
