class MyCalendarTwo:
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True

Cld = MyCalendarTwo()
print (Cld.book(10, 20))
print (Cld.book(50, 60))
print (Cld.book(10, 40))
print (Cld.book(5, 15))
print (Cld.book(5, 10))
print (Cld.book(25, 55))