class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """

        """
        from collections import Counter
        counted_nums = Counter(nums)
        return counted_nums.most_common(1)[0][0]