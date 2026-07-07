class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        # Count frequencies
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort by frequency (highest first)
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Take first k elements
        result = []

        for i in range(k):
            result.append(sorted_freq[i][0])

        return result