class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Store the currentSum as numbers[left] + numbers[right]
            - (the converging ends of the array)
        If the currentSum is greater than the target:
            - Decrement right to shrink
        If the currentSum is less than the target:
            - Increment left to expand
        If currentSum == target:
            - Return [left + 1, right + 1] (as 1-indexed)
                - (not the elements but the indices)
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]
            if currentSum == target:
                return [left + 1, right + 1]
            elif currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
            