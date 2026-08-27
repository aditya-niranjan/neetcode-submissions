class Solution:
    def maxSlidingWindow(self, nums, k):

        dq = deque()
        res = []

        for right in range(len(nums)):

            # Remove indices that are outside the window
            if dq and dq[0] < right - k + 1:
                dq.popleft()

            # Remove smaller values from the back
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            # Add current index
            dq.append(right)

            # Window is ready
            if right >= k - 1:
                res.append(nums[dq[0]])

        return res