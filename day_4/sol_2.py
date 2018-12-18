import sys
import re
import datetime
from collections import defaultdict
import numpy as np
from copy import deepcopy

NEW_GUARD = re.compile('Guard #(\d+) begins shift')

events = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        date = datetime.datetime.strptime(line[:18], '[%Y-%m-%d %H:%M]')
        m = NEW_GUARD.search(line)
        if m is not None:
            events.append((deepcopy(date), int(m.group(1))))
        elif 'falls asleep' in line:
            events.append((date, 'falls asleep'))
        elif 'wakes up' in line:
            events.append((date, 'wakes up'))

events.sort()
sleepy_time = defaultdict(lambda: np.zeros(60))
guard = 0
for i, (date, event) in enumerate(events):
    if type(event) is int:
        guard = event
        continue
    if event == 'wakes up':
        prev_date = events[i-1][0]
        print(guard, prev_date.minute, date.minute)
        sleepy_time[guard][prev_date.minute:date.minute] += 1

guard_sleep = {time.max(): guard for guard, time in sleepy_time.items()}
print(guard_sleep)
maximum_sleep = max(guard_sleep)
sleepy_guard = guard_sleep[maximum_sleep]
print(sleepy_guard)
print(sleepy_time[sleepy_guard])
print(sleepy_time[sleepy_guard].argmax())
print(sleepy_guard * sleepy_time[sleepy_guard].argmax())
