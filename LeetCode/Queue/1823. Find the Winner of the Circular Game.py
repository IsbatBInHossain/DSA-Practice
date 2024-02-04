class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        current = 0
        arr = [i+1 for i in range(n)]
        while len(arr) > 1:
            current = (current + k -1) % len(arr) 
            arr.remove(arr[current])
        return arr[0]