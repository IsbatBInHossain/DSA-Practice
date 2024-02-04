from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(students)
        sandwiches_queue = deque(sandwiches)
        count = 0
        while sandwiches_queue:
            if count >= 2 * len(students):
                break
            if students_queue[0] == sandwiches_queue[0]:
                students_queue.popleft()
                sandwiches_queue.popleft()
                count -= 1
            else:
                student = students_queue.popleft()
                students_queue.append(student)
                count += 1
        return len(students_queue)
