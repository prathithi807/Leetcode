from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Step 1: push x into q2
        self.q2.append(x)
        # Step 2: move all elements from q1 → q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Step 3: swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()   # front of q1 is the "top" of stack

    def top(self) -> int:
        return self.q1[0]   # front of q1 is the "top"

    def empty(self) -> bool:
        return not self.q1

