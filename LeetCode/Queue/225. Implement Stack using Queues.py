from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        current, other = (self.q1, self.q2) if self.q1 else (self.q2, self.q1)

        while len(current) > 1:
            other.append(current.popleft())

        return current.popleft()
        

    def top(self) -> int:
        current, other = (self.q1, self.q2) if self.q1 else (self.q2, self.q1)

        while len(current) > 1:
            other.append(current.popleft())

        top_element = current[0]
        other.append(current.popleft()) 

        return top_element  
        

    def empty(self) -> bool:
        return not self.q1 and not self.q2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()