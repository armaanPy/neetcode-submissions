class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Initialise map
        Find complement
        If complement is in the map:
            return indices
        Else:
            add num key with indice value to map
        """
        num_map = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], idx]
            num_map[num] = idx