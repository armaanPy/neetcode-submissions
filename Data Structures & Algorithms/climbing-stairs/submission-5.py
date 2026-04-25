class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 2 3 4 5
        # 8  5  3  2  1  1
        # ^ans

        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one