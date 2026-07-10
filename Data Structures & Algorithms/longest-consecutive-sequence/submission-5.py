class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = sorted(list(set(nums)))
        res = 1
        for i in range(len(nums)):
            idx = i
            for j in range(i+1,len(nums)):
                if nums[j] - nums[idx] == 1:
                    res = max(res, j - i + 1)
                    idx = j
                else:
                    break
        return res