class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash = {}
        for num in nums:
            if num in hash:
                hash[num]+=1
            else:
                hash[num] = 1
        
        # Sort the dictionary items by value (frequency) in descending order
        sorted_items = sorted(hash.items(), key=lambda x: x[1], reverse=True)
        
        result = []
        # Take the first k keys from the sorted list
        for i in range(k):
            result.append(sorted_items[i][0])

        return result