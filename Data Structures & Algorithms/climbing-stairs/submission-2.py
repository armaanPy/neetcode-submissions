class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 5
        # 0  1      2       3       4       5
        # 8  5       3        2        1        1

        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one