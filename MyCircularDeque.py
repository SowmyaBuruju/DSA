import unittest

class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.queue = [-1] * k  # Initialize deque with size k
        self.front = 0  # Front pointer
        self.rear = -1  # Rear pointer
        self.size = 0   # Tracks current elements count

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.k) % self.k  # Move front pointer left
        self.queue[self.front] = value
        if self.size == 0:  # If first element, sync rear
            self.rear = self.front
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.k  # Move rear pointer right
        self.queue[self.rear] = value
        if self.size == 0:  # If first element, sync front
            self.front = self.rear
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = -1  # Optional: Clear the value
        self.front = (self.front + 1) % self.k  # Move front pointer right
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.rear] = -1  # Optional: Clear the value
        self.rear = (self.rear - 1 + self.k) % self.k  # Move rear pointer left
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


class TestMyCircularDeque(unittest.TestCase):
    def test_case_1(self):
        myCircularDeque = MyCircularDeque(3)

        # Given test cases
        operations = [
            ("insertLast", 1, True),   # ✅ return True
            ("insertLast", 2, True),   # ✅ return True
            ("insertFront", 3, True),  # ✅ return True
            ("insertFront", 4, False), # ❌ return False (Deque is full)
            ("getRear", None, 2),      # ✅ return 2
            ("isFull", None, True),    # ✅ return True
            ("deleteLast", None, True),# ✅ return True
            ("insertFront", 4, True),  # ✅ return True
            ("getFront", None, 4)      # ✅ return 4
        ]

        for operation, value, expected in operations:
            if value is None:
                result = getattr(myCircularDeque, operation)()
            else:
                result = getattr(myCircularDeque, operation)(value)
            
            self.assertEqual(result, expected, f"Failed at {operation}({value})")

if __name__ == "__main__":
    unittest.main()
