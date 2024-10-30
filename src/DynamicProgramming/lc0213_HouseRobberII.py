# https://leetcode.cn/problems/house-robber-ii
class Solution:
    def rob(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        # dp_0[i] 代表考虑完下标为i的那一家受害者之后盗贼能够拥有的最大赃物总价值信息
        # dp_0[i][1] 代表考虑完下标为i的那一家受害者并抢了他之后盗贼能够拥有的最大赃物总价值
        # dp_0[i][0] 代表考虑完下标为i的那一家受害者并放过他之后盗贼能够拥有的最大赃物总价值

        # 考虑最后一家受害者的时候不知道前一家的最优解中第一家偷了没有偷
        # 所以将第一家偷和第一家不偷的情况分别考虑求最优解

        # 第一家不偷, 最后一家可以正常偷或不偷
        dp_0: list[list[int | None]] = [[None, None] for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                dp_0[i][0] = 0
                dp_0[i][1] = None
            elif i == 1:
                dp_0[i][0] = 0 + 0
                dp_0[i][1] = 0 + nums[i]
            else:
                dp_0[i][0] = max(dp_0[i-1][0], dp_0[i-1][1]) + 0
                dp_0[i][1] = dp_0[i-1][0] + nums[i]

        # 第一家偷, 最后一家不偷
        dp_1: list[list[int | None]] = [[None, None] for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                dp_1[i][0] = None
                dp_1[i][1] = nums[i]
            elif i == 1:
                dp_1[i][0] = nums[i-1] + 0
                dp_1[i][1] = nums[i-1] + 0
            elif i == len(nums) - 1:
                dp_1[i][0] = max(dp_1[i-1][0], dp_1[i-1][1]) + 0
                dp_1[i][1] = None
            else:
                dp_1[i][0] = max(dp_1[i-1][0], dp_1[i-1][1]) + 0
                dp_1[i][1] = dp_1[i-1][0] + nums[i]

        return max(max(dp_0[len(nums) - 1][0],
                       dp_0[len(nums) - 1][1]),
                   dp_1[len(nums) - 1][0])
