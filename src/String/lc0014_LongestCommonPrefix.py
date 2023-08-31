# https://leetcode.cn/problems/longest-common-prefix
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) <= 0:
            raise "Invalid Input strs"
        min_length = min((len(x) for x in strs))
        chars: list[str] = [''] * min_length
        for index in range(min_length):
            chars[index] = strs[0][index]
            for string in strs:
                if string[index] != chars[index]:
                    return ''.join(chars[0: index])
        return ''.join(chars)
