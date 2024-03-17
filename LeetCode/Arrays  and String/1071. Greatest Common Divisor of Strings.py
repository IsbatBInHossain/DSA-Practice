class Solution:
    def stringDivision(self, dividend: str, divisor: str) -> str or None: # type: ignore
        if dividend == divisor:
            return divisor
        for i in range(len(divisor)):
            if dividend[i] != divisor[i]:
                return None
        remainder = dividend.replace(divisor, '', 1)
        if len(remainder) >= len(divisor):
            return self.stringDivision(remainder, divisor)
        else:
            return self.stringDivision(divisor, remainder)
                
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        gcd = self.stringDivision(str1, str2)

        return '' if gcd is None else gcd
        

        