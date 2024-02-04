from collections import deque
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets_queue = deque(tickets)
        time = 0
        while tickets_queue:
            t = tickets_queue.popleft() - 1
            time+=1
            if k == 0 and t == 0:
                break
            if t > 0:
                tickets_queue.append(t)
            k = (k-1) if (k-1) >=0 else len(tickets_queue) - 1
        return time