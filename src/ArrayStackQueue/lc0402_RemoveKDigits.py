# https://leetcode.cn/problems/remove-k-digits

# 让我们从一个简单的例子开始。
# 给定一个数字序列，例如 425，如果要求我们只删除一个数字，那么从左到右，我们有 4、2 和 5 三个选择。
# 我们将每一个数字和它的左邻居进行比较。
# 从 2 开始，2 小于它的左邻居 4。假设我们保留数字 4，那么所有可能的组合都是以数字 4（即 42，45）开头的。
# 相反，如果移掉 4，留下 2，我们得到的是以 2 开头的组合（即 25），这明显小于任何留下数字 4 的组合。
# 因此我们应该移掉数字 4。如果不移掉数字 4，则之后无论移掉什么数字，都不会得到最小数。
#
# 基于上述分析，我们可以得出「删除一个数字」的贪心策略：
#
# 给定一个长度为 n 的数字序列 [D0 D1 D2 D3… Dn−1]，
# 从左往右找到第一个位置 i（i>0）使得 Di−1 > Di，并删去 Di−1；如果不存在，说明整个数字序列单调不降，删去最后一个数字即可。
#
# 基于此，我们可以每次对整个数字序列执行一次这个策略；
# 删去一个字符后，剩下的 n−1 长度的数字序列就形成了新的子问题，
# 可以继续使用同样的策略，直至删除 k 次。
#
# 暴力的实现复杂度最差会达到 O(nk)（考虑整个数字序列是单调不降的）。

class Solution:

    # # 暴力
    # def removeKdigits(self, num: str, k: int) -> str:
    #     if len(num) == k:
    #         return "0"
    #     if len(num) < k:
    #         raise "Invalid Input"
    #
    #     digits: list[str] = list(num)
    #
    #     n_times: int = k
    #     while n_times > 0:
    #         index: int = 0
    #         while index + 1 <= len(digits) - 1 and digits[index] <= digits[index + 1]:
    #             index += 1
    #         if index + 1 <= len(digits) - 1:  # found digits[index] > digits[index + 1]
    #             digits.pop(index)
    #         else:
    #             digits.pop()
    #         n_times -= 1
    #
    #     while len(digits) > 0 and digits[0] == "0":
    #         digits.pop(0)
    #     if len(digits) == 0:
    #         return "0"
    #     return "".join(digits)

    # 非暴力，单调栈。
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        if len(num) < k:
            raise "Invalid Input"

        digits: list[str] = list(num)

        # 代码从这里开始不一样
        removed_digits: list[str] = []

        # 栈底元素小，栈顶元素大于或等于栈底元素。构造这个栈的时候最先弹出的K个元素就是要删除的个元素。
        # 单调栈的栈元素是 ElementValue
        remaining_digits: list[str] = []

        for digit in digits:
            while len(removed_digits) < k and (len(remaining_digits) > 0 and remaining_digits[-1] > digit):
                removed_digits.append(remaining_digits[-1])
                remaining_digits.pop()
            remaining_digits.append(digit)

        if len(removed_digits) < k:
            remaining_digits = remaining_digits[:-(k - len(removed_digits))]

        digits = remaining_digits
        # 不一样的地方结束

        while len(digits) > 0 and digits[0] == "0":
            digits.pop(0)
        if len(digits) == 0:
            return "0"
        return "".join(digits)
