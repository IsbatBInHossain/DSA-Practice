class Solution:
    def isVowel(self, c: str) -> bool:
        # Check if the character is a vowel
        vowels = list('aeiou')
        return c in vowels
    
    def adjustCount(self, prev: str, current: str, count: int) -> int:
        # Adjust the vowel count based on changes from previous to current substring
        if self.isVowel(prev[0]):
            count -= 1
        if self.isVowel(current[-1]):
            count += 1
        return count

    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        # Initialize count with vowels in the first substring
        count = 0
        prev = s[:k]
        for c in prev:
            if self.isVowel(c):
                count += 1

        max_count = count
        # Iterate over the substrings of length k starting from the second substring
        for i in range(1, n - k + 1):
            current = s[i:i+k]
            # Adjust the count based on changes from previous to current substring
            count = self.adjustCount(prev, current, count)
            prev = current
            # Update the maximum count of vowels encountered so far
            max_count = max(count, max_count)

        return max_count
