class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        pdArray = []
        pd = ""
        stack = 0
        for c in s:
            if c == "(":
                stack += 1
                pd +="("
            else:
                stack -= 1
                pd += ")"
            if stack == 0:
                pdArray.append(pd[1:len(pd)-1])
                pd = ""
        return ''.join(map(str, pdArray))