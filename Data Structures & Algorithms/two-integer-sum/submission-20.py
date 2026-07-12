class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference in num_map:
                return [num_map[difference], index]
            num_map[num] = index