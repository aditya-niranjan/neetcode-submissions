class Solution:
    def findLucky(self, arr: List[int]) -> int:
        map  = {}

        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1


        lacky = -1

        for num in freq:
            if num == freq[num]:
                lacky = max(lacky,num)

        return lacky