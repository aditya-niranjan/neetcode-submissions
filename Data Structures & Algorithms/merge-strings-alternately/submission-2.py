class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = ""
        i = 0

        while i < len(word1) or i < len(word2):

            if  len(word1) == 0:
                result += word1[i:]
                break

            if len(word2) == 0:
                result += word2[i:]
                break

            if i < len(word1):
                result+=word1[i]

            if i < len(word2):
                result+=word2[i]

            i += 1

        return result