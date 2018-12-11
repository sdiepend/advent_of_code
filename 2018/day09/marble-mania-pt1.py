from collections import defaultdict

no_players = 405
last_marble = 71700

scores = defaultdict(lambda: 0)
circle = [0, 1]
current = 1
for i in range(2, last_marble+1):
    if i % 23 == 0:
        scores[i % no_players] += i + circle[current - 7]
        current = (current - 7) % len(circle)
        circle.pop(current)
    else:
        current = (current + 2) % len(circle)
        if current == 0:
            current = len(circle)
            circle.append(i)
        else:
            circle.insert(current, i)

max_score = max(scores.values())

print(max_score)
