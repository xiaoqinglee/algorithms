class Solution:

    # 剑指 Offer 10- II. 青蛙跳台阶问题
    # https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
    def numWays(self, n: int) -> int:

        # 台阶有n级，将它抽象为一个length为n+1的数组。 index：0..n
        # 问题：站在index==0位置开始，跳到index==n的位置有多少种跳法？

        # 子问题：
        # 0 < m < n, 已知从m位置和m后面的位置跳到index==n的位置有多少种跳法，
        # 求从m-1位置跳到index==n的位置有多少种跳法？
        # 把后半程定义为子问题，缓存后半程的结果，逐步膨胀后半程。

        # dp[i]代表从index i跳跃到index n的跳法数目。
        dp: list[int | None] = [None] * (n + 1)
        for i in range(n, -1, -1):
            if i == n:
                n_ways = 1
                dp[i] = n_ways
            elif i == n - 1:
                n_ways = 1
                dp[i] = n_ways
            else:
                dp[i] = dp[i + 1] + dp[i + 2]

        # return dp[0]
        # 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
        return dp[0] % (10 ** 9 + 7)

    # lc 55. Jump Game
    # https://leetcode.cn/problems/jump-game/
    def canJump(self, nums: list[int]) -> bool:

        # 给定一个非负整数数组 nums ，你最初位于数组的 第1个下标 。
        # 数组中的每个元素代表你在该位置可以跳跃的最大长度。
        # 判断你是否能够到达最后一个下标。

        # 仍然将将后半程作为子问题，缓存子问题的结果，并膨胀子问题，
        # 与 self.numWays()不同的是台阶的元素数目是n( len(nums) )而不是n+1

        # # 子问题：
        # 0 < m < n-1, 已知从m位置和m后面的位置能否跳到index==n-1的位置（true：能，false：不能），
        # 求从m-1位置能否跳到index==n-1的位置？

        # dp[i]代表从index i是否可以跳跃到index n-1。
        dp: list[bool | None] = [None] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                dp[i] = True
            else:
                max_n_steps = nums[i]
                for n_steps in range(1, max_n_steps + 1):
                    target_index = i + n_steps
                    if target_index <= len(nums) - 1 and dp[target_index] is True:
                        dp[i] = True
                        break
                if dp[i] is not True:
                    dp[i] = False

        return dp[0]

    # 45. 跳跃游戏 II
    # https://leetcode.cn/problems/jump-game-ii/
    def jump(self, nums: list[int]) -> int | None:

        # 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
        # 数组中的每个元素代表你在该位置可以跳跃的最大长度。
        # 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
        # 假设你总是可以到达数组的最后一个位置。
        # 求这个最小跳跃次数。

        # 仍然将将后半程作为子问题，缓存子问题的结果，并膨胀子问题，
        # 台阶的元素数目是n( len(nums) )

        # # 子问题：
        # 0 < m < n-1, 已知从m位置和m后面的位置跳到index==n-1的位置使用的最小跳跃次数，
        # 求从m-1位置跳到index==n-1的位置使用的最小跳跃次数。

        # dp[i]代表从index i跳跃到index n-1有最小跳跃数的那个跳法的跳跃数。
        # 如果找不到一个能够跳跃到index n-1的跳法，那么dp[i] is None.
        dp: list[int | None] = [None] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                dp[i] = 0
            else:

                # 每一个元素代表一个跳跃方案， 元素的值代表该方案的跳跃数。
                jump_choices: list[int] = []

                max_n_steps = nums[i]
                for n_steps in range(1, max_n_steps + 1):
                    target_index = i + n_steps
                    if target_index <= len(nums) - 1 and dp[target_index] is not None:
                        jump_choices.append(dp[target_index])

                if len(jump_choices) == 0:
                    fewest_n_jumps = None
                else:
                    fewest_n_jumps = 1 + min(jump_choices)
                dp[i] = fewest_n_jumps

        return dp[0]

    # 746. 使用最小花费爬楼梯
    # https://leetcode.cn/problems/min-cost-climbing-stairs/
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        # 仍然将将后半程作为子问题，缓存子问题的结果，并膨胀子问题，
        # 台阶的元素数目是n( len(nums) )

        # 台阶的坐标为 0..n-1，初始位置为-1，最终位置为n。 数组中被踏过的元素会被计费。

        # # 子问题：
        # 0 < m < n-1, 已知从m位置和m后面的位置跳到最终位置使用的某一跳跃方案具有的最小成本金额，
        # 求从m-1位置跳到最终位置使用的最小成本金额。

        # dp[i]代表从index i跳跃到最终位置有最小成本金额的跳跃方案对应的最小成本金额。
        # 因为每个位置都能跳一步或两步，所以每个位置都至少有一个够跳跃到最终位置的跳法，所以最终dp[i] is not None.
        dp: list[int | None] = [None] * (len(cost) + 1)

        for i in range(len(cost), -1, -1):  # 注意i的值考虑 n
            if i == len(cost):
                dp[i] = 0
            elif i == len(cost) - 1:
                dp[i] = cost[i]
            elif i == len(cost) - 2:
                # cost元素的值都是正数
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        return min(dp[0], dp[1])
