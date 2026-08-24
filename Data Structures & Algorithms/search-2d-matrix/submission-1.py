class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = matrix
        row = len(nums)
        cols = len(nums[0])

        if row == 0 and col == 0 :
            return False

        for i in range(row):
            curr = nums[i]
            low = 0
            high =  len(curr)-1

            while low<=high:
                mid = int(low + (high - low)/2)

                if curr[mid] == target:
                    return True
                elif curr[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
        return False