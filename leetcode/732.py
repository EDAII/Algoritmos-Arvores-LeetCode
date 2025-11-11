class MyCalendarThree:
    def __init__(self):
        self.events = SortedDict()
    
    def book(self, startTime: int, endTime: int) -> int:
        self.events[startTime] = self.events.setdefault(startTime, 0) + 1
        self.events[endTime]   = self.events.setdefault(endTime, 0)   - 1

        nbook, maxbook = 0, 0

        for time in self.events:
            nbook += self.events[time]
            maxbook = max(maxbook, nbook)

        return maxbook