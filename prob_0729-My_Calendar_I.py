from bisect import bisect

class MyCalendar:

    def __init__(self):
        self.windows = [] # array of tuples
        
    def book(self, start: int, end: int) -> bool:
        win = (start, end)
        if not self.windows:
            self.windows.append(win)
            return True
        
        idx = bisect(self.windows, win)
        if idx < len(self.windows):
            if end > self.windows[idx][0]:
                return False
        if idx > 0:
            if start < self.windows[idx-1][1]:
                return False

        self.windows.insert(idx, win)
        return True

## Test
obj = MyCalendar()
print(obj.book(10, 20))
print(obj.book(15, 25))
print(obj.book(20, 30))
print(obj.book(1, 7))
print(obj.book(4, 20))
