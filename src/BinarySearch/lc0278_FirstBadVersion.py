# https://leetcode.cn/problems/first-bad-version
class Solution:

    # # 递归版本
    # def firstBadVersion(self, n: int) -> int:
    #
    #     # # 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
    #     # # 你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。
    #     #
    #     # def isBadVersion(version: int) -> bool:
    #     #     pass
    #
    #     def traverse(left_pointer: int, right_pointer: int) -> int:
    #         if left_pointer == right_pointer:
    #             return left_pointer
    #         mid_pointer: int = (left_pointer + right_pointer) // 2
    #         if isBadVersion(mid_pointer):
    #             return traverse(left_pointer, mid_pointer)
    #         else:
    #             return traverse(mid_pointer + 1, right_pointer)
    #
    #     return traverse(1, n)


    # 迭代版本
    def firstBadVersion(self, n: int) -> int:

        # def isBadVersion(version: int) -> bool:
        #     pass

        left_pointer: int = 1
        right_pointer: int = n
        while True:
            if left_pointer == right_pointer:
                return left_pointer
            mid_pointer: int = (left_pointer + right_pointer) // 2
            if isBadVersion(mid_pointer):
                right_pointer = mid_pointer
            else:
                left_pointer = mid_pointer + 1

# 总结：
#
#     如果我们寻找的是第一个坏版本， 那么我们要保持当前窗口中一定存在第一个坏版本，
#         如果中间元素是坏版本，那么要将它留在窗口中，因为他可能是第一个坏版本。
#         如果中间元素是好版本，那么不要把他留在窗口中，因为他不是坏版本所以不可能是第一个坏版本。
