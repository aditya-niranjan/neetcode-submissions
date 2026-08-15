class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # freq = {}

        # for num in arr:
        #     freq[num] = freq.get(num, 0) + 1


        # lacky = -1

        # for num in freq:
        #     if num == freq[num]:
        #         lacky = max(lacky,num)

        # return lacky

            freq = [0] * 501

            for num in arr:
                freq[num] += 1

            for num in range(500, 0, -1):
                if freq[num] == num:
                    return num

            return -1

            