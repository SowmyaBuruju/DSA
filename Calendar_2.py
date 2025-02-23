import unittest

class MyCalendarTwo:
    def __init__(self):
        self.calendar = []  # Stores single bookings
        self.overlaps = []  # Stores double bookings

    def book(self, startTime: int, endTime: int) -> bool:
        # Step 1: Check if this event would cause a triple booking
        for os, oe in self.overlaps:
            if max(startTime, os) < min(endTime, oe):  # Overlapping condition
                return False  # Triple booking would occur
        
        # Step 2: Check for new overlaps with existing bookings
        for cs, ce in self.calendar:
            if max(startTime, cs) < min(endTime, ce):  # Overlapping condition
                self.overlaps.append((max(startTime, cs), min(endTime, ce)))
        
        # Step 3: Add event to the calendar
        self.calendar.append((startTime, endTime))
        return True

class TestMyCalendarTwo(unittest.TestCase):
    def test_calendar(self):
        myCalendarTwo = MyCalendarTwo()
        
        # Given test cases
        test_cases = [
            (10, 20, True),   # ✅ The event can be booked.
            (50, 60, True),   # ✅ The event can be booked.
            (10, 40, True),   # ✅ The event can be double booked.
            (5, 15, False),   # ❌ Triple booking occurs.
            (5, 10, True),    # ✅ The event can be booked.
            (25, 55, True)    # ✅ No triple booking, valid booking.
        ]

        for start, end, expected in test_cases:
            with self.subTest(start=start, end=end):
                self.assertEqual(myCalendarTwo.book(start, end), expected)

if __name__ == "__main__":
    unittest.main()
