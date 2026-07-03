class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return the indices; i, j - whose values sum up to target
        Algo:
        - Initialise a HashMap
        - Iterate through the index, num of values in num
        - Calculate the difference we need: target - num
        - Add each num and its index (in nums) to HashMap
        - If the difference (of the current num) is in the hashMap then return
          the pair of indices
        """
        trackMap = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference in trackMap:
                return [trackMap[difference], index]
            trackMap[num] = index