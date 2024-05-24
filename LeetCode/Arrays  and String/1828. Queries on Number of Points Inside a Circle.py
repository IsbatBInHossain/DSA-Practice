import math
from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answers = []
        for circle in queries:
            count = 0
            for point in points:
                distance = math.sqrt((circle[0] - point[0])**2 + (circle[1] - point[1])**2)
                if distance <= circle[2]:
                    count += 1
            answers.append(count)
        
        return answers
        