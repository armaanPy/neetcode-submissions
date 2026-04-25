class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums * 2
        # return ans
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans