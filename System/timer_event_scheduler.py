import time

class TimerEventScheduler:
    class _TimerEvent:
        mFunction = None # Function Callback
        mDelay = None # Delay in Time between start of previous execution and start of next execution
        mNextExecution = None # Earliest timestamp that the event will be executed (updated during each run)

        def __init__(self, function, delay):
            self.mFunction = function
            self.mDelay = delay
            self.mNextExecution = 0

    mEvents = None # Array of TimerEvent

    def __init__(self):
        self.mEvents = []

    # Users should use the 'partial' function to bind all arguments to the function callback
    # Delay is in seconds (float)
    # Time Precision is 10 milliseconds
    def add_event(self, function, delay):
        self.mEvents.append(TimerEventScheduler._TimerEvent(function, delay))

    def update(self):
        # Gets current timestamp
        t = time.time()

        # Loops through each of the events and runs them if necessary
        for i in range(0, len(self.mEvents)):
            if self.mEvents[i].mNextExecution < t:
                # Run the Event
                self.mEvents[i].mFunction()

                # If it's the 1st time calling, set the initial execution time to the current time
                if self.mEvents[i].mNextExecution == 0:
                    self.mEvents[i].mNextExecution = t

                # Add the delay for the next time it runs
                self.mEvents[i].mNextExecution = self.mEvents[i].mNextExecution + self.mEvents[i].mDelay
