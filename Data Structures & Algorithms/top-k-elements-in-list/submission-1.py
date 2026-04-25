class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counter({3: 3, 2: 2, 1: 1})
        count = Counter(nums)
        return [integer for integer, occurence in count.most_common(k)]
        