class Solution:
    def isVowel(self, c:str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']

        if c.lower() in vowels:
            return True
        return False


    def reverseVowels(self, s: str) -> str:
        first = 0
        last = len(s) - 1
        s_array = list(s)

        while (last > first):
            while last > first and not self.isVowel(s_array[first]):
                first += 1
            while last > first and not self.isVowel(s_array[last]):
                last -= 1
            else:
                s_array[first], s_array[last] = s_array[last], s_array[first]
                first += 1
                last -= 1
         
        return ''.join(map(str, s_array))
        