class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sentence = [None]*len(words)
        pos = [int(c[-1])-1 for c in words]
        for i in range(len(words)):
            sentence[pos[i]] = words[i][:-1]

        return ' '.join(sentence)