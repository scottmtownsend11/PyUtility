# No Bytecode
import sys
sys.dont_write_bytecode = True
sys.path.append('..')

# System
import time
from functools import partial

# Local
from timer_event_scheduler import TimerEventScheduler

def get_timestamp():
    return time.time()

def f1():
    print get_timestamp(), 'Every 5 seconds'

def f2(a):
    print get_timestamp(), 'Every 1 second', '    ID:', a

def f3(a, b, c):
    print get_timestamp(), 'Every 250 milliseconds', '    ID:', a, b, c

RUN_TIME = 15 # seconds

# Setup Scheduler
scheduler = TimerEventScheduler()
scheduler.add_event(f1, 5)
scheduler.add_event(partial(f2,2), 1)
scheduler.add_event(partial(f3,3,4,5), 0.25)

# Run Scheduler
start = get_timestamp()
while get_timestamp() < start + RUN_TIME:
    scheduler.update()

print("\nSuccess!")
