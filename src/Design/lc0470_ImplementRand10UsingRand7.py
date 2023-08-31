# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


# https://leetcode.cn/problems/implement-rand10-using-rand7/
class Solution:

    def __rand2(self) -> int:
        while True:
            r = rand7()
            if 1 <= r <= 3:
                return 1
            elif 4 <= r <= 6:
                return 2
            else:
                # do nothing
                pass

    def __rand5(self) -> int:
        while True:
            r = rand7()
            if 1 <= r <= 5:
                return r
            else:
                # do nothing
                pass

    def rand10(self) -> int:
        r1 = self.__rand2()
        r2 = self.__rand5()
        if r1 == 1:
            return 2 * r2 - 1
        else:
            return 2 * r2
