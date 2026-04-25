class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1 2 2 3 3 3 . k2
        #Counter({3: 3, 2: 2, 1: 1})
        count = Counter(nums)
        
        res = [val for val, occurrence in count.most_common(k)]

        return res