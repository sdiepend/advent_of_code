import re
from collections import defaultdict
from datetime import datetime
from operator import itemgetter

with open("input.txt") as f:
    content = f.readlines()

log = []
for line in content:
    y, m, d, h, minute, message = re.match(r'^\[(\d+)-(\d+)-(\d+)\s(\d+)\:(\d+)\]\s(.*)$', line).groups()
    log.append([datetime(int(y), int(m), int(d), int(h), int(minute))] + message.split())


records = sorted(log, key=itemgetter(0))

shifts = defaultdict(lambda: [0 for i in range(60)])
guard = ''
start_asleep = 0
end_asleep = 0
for record in records:
    if record[1] == 'Guard':
        guard = record[2]
    if record[1] == 'falls':
        start_asleep = record[0].minute
    if record[1] == 'wakes':
        end_asleep = record[0].minute
        for i in range(start_asleep, end_asleep):
            shifts[guard][i] += 1

most_asleep_guard = ''
highest_value = 0
minute = 0

for guard, shift in shifts.items():
    total_asleep = sum(shift)

    if total_asleep >= highest_value:
        highest_value = total_asleep
        most_asleep_guard = guard.strip('#')
        max_value = max(shift)
        minute = shift.index(max_value)
print(minute * int(most_asleep_guard))

most_freq_min_guard = ''
highest_freq = 0
highest_freq_min = 0
for guard, shift in shifts.items():
    max_freq = max(shift)
    if max_freq > highest_freq:
        highest_freq = max_freq
        highest_freq_min = shift.index(max_freq)
        most_freq_min_guard = guard.strip('#')

print(highest_freq_min * int(most_freq_min_guard))

    
