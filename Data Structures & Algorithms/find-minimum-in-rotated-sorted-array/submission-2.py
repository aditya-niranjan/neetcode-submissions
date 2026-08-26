class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums)-1
        mini = float("inf")
        while low<=high:

            mid = (low + high) //2

            if nums[low] <= nums[mid]:
                mini = min(mini,nums[low])
                low = mid+1
            elif nums[mid] <= nums[high]:
                high = mid - 1
                mini = min(mini,nums[mid])


        return mini