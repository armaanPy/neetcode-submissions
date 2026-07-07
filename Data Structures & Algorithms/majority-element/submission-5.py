class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Given an array, return the element that appears the most 
            (more than half)
        
        Algo 1 - O(n) T
        - Create a dict
        - Iterate through nums and add each value, occurrence to dict
        - Return key with largest value

        Algo 2 - Counter
        - Use Counter from collections
        
        Algo 3 - O(1)
        - 
        """
        from collections import Counter
        
        count = Counter(nums)
        return count.most_common(1)[0][0]