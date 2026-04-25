class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # # Simple method
        # ans = nums * 2
        # return ans

        # Array Algorithm method
        ans = []
        for i in range(2):
            for i in nums:
                ans.append(i)
        return ans