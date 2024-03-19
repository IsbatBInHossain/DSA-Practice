from collections import Counter
from typing import List


class Solution:
    def find_max_frequency(self, data: List[int])-> tuple[int, int]: 
        frequency_map = Counter(data)

        max_frequency = max(frequency_map.values(), default=0)
        count = 0
        for value in frequency_map.values():
            if value == max_frequency:
                count += 1

        return max_frequency, count


    def leastInterval(self, tasks: List[str], n: int) -> int:
        totalJobs = len(tasks)
        max_freq, count = self.find_max_frequency(tasks)
        return max((n+1)*(max_freq-1)+ count , totalJobs)

        