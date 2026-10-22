class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        nums = [3,4,5,6]    target = 7
        -> 0, 1
        Return the indices of the (2) num in nums that equal target

        - Create an empty dict
        - Enumerate through the index, num of nums
        - Store complement as: target - num (this will give us the number we need to find)
        - Add the num (key) and index (value) to the dict
        - Check if complement is in the num, if it is:
            - Return the index value from dict, and current index as a list
        """
        num_map = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], index]
            num_map[num] = index