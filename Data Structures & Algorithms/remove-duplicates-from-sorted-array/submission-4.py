class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums is in asc order
        # remove dupes in place, so each element appears only once
        # after removing, return num of unique elements (k)

        # 1 1 2 3 4
        #   L
        #   R
        # if R doesnt equal R - 1 -> good, push R to L
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        
        return l