class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # put nums into a dict
        # each time a num is seen, increment dict by 1
        # actually, use counter
        
        # Counter({3: 3, 2: 2, 1: 1})
        count = Counter(nums)
        mc = [element for element, occurrence in count.most_common(k)]

        return mc