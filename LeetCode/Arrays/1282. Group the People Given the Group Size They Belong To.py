from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupMap = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in groupMap:
                groupMap[groupSizes[i]].append(i)
            else:
                groupMap[groupSizes[i]] = [i]
        
        groups = []
        for key, value in groupMap.items(): 
            n = key 
            if n == len(value):  
                groups.append(value)
            else:
                m = len(value) // n
                groups.extend([value[i*n:(i+1)*n] for i in range(m)])
        return groups
