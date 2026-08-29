class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key, value, timestamp):
        if key not in self.mp:
            self.mp[key] = []

        self.mp[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.mp:
            return ""

        arr = self.mp[key]

        left = 0
        right = len(arr) - 1

        ans = ""

        while left <= right:

            mid = (left + right) // 2

            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                left = mid + 1

            else:
                right = mid - 1

        return ans