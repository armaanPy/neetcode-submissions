class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1 2 2 3 3 3 | k = 2
        # {1:1, 2:2, 3:3}
        #  ^val
        #         ^occurence 
        count = Counter(nums)
        res = [value for value, occurence in count.most_common(k)]
        return res

