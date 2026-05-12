class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        [1 1 0 1 1 1] -> 3
         1 2 0 1 2 3

        Have two counters: current_count and maximum_count
        Iterate through the array, when a '1' is seen, increment current_count
        When a '0' is seen, get the max() of current_count and maximum_count
        return that max 
        
        [1 1 0 1 1 1]
        curr = 0 (start)
        curr = 1
        curr = 2
        0 reached
        max(curr, curr_max) | 2
        curr = 0 (reset)
        curr = 1
        curr = 2
        curr = 3
        max(curr, curr_max) | 3
        """
        curr_count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                curr_count += 1
                max_count = max(curr_count, max_count)
            else:
                curr_count = 0
        return max_count
