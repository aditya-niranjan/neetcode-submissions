class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = ""
        i = 0
        wod1 = len(word1)
        wod2 = len(word2)
        while i < len(word1) or i < len(word2):

            if  len(word1) == 0:
                result += word1[i:]
                break

            if len(word2) == 0:
                result += word2[i:]
                break

            if i < len(word1):
                result+=word1[i]
                wod1-=1

            if i < len(word2):
                result+=word2[i]
                wod2-=1

            i += 1

        return result