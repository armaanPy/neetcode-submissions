class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        
        count = Counter(nums)
        res = []
        for element, freq in count.most_common(k):
            res.append(element)
        return res
