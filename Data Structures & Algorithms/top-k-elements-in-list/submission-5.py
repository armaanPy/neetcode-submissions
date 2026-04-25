class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1 2 2 3 3 3 | k = 2
        #Counter({3: 3, 2: 2, 1: 1})
        count = Counter(nums)
        res = [element for element, occurrence in count.most_common(k)]
        return res