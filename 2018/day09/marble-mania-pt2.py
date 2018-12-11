from collections import defaultdict, deque

no_players = 405
last_marble = 71700 * 100

scores = defaultdict(lambda: 0)
circle = deque([0, 1])
for i in range(2, last_marble+1):
    if (i % 23) == 0:
        circle.rotate(7)
        scores[i % no_players] += i + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(i)

max_score = max(scores.values())

print(max_score)
