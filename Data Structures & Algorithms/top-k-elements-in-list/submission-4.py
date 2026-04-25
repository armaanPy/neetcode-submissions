class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = [element for element, occurrence in count.most_common(k)]
        return res