class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Set two converging pointers at both ends of the array
        Set currentSum to be sum of two pointers
        If answer == target, return
        If answer > target, shift right pointer back
        If answer < target, shift left pointer forward
        return pointers + 1 (as we need to return 1-indexed)
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                return [left + 1, right + 1]
            elif currentSum > target:
                right -= 1
            else:
                left += 1