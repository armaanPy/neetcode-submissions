class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty map
        # Loop through the index and value of nums
        # Calculate the complement from the target
        # Check if the target exists in the map
        # If yes, return the index
        num_map = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_map:
                return [num_map[complement], i]
            num_map[n] = i