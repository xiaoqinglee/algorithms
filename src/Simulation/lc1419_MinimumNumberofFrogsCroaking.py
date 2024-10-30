from collections import defaultdict

Char = str

# https://leetcode.cn/problems/minimum-number-of-frogs-croaking

# class Frog:
#     CROAK = "croak"
#
#     def __init__(self):
#         self.__next_croak_char_index = 0
#
#     def croak_one_char(self, char: Char) -> bool:
#         if char == Frog.CROAK[self.__next_croak_char_index]:
#             self.__next_croak_char_index = (self.__next_croak_char_index + 1 + len(Frog.CROAK)) % len(Frog.CROAK)
#             return True
#         return False
#
#     def can_mute(self) -> bool:
#         return self.__next_croak_char_index == 0
#
#     def next_croak_char(self):
#         return Frog.CROAK[self.__next_croak_char_index]
#
#
# # https://leetcode.cn/problems/minimum-number-of-frogs-croaking
# class Solution:
#     def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
#
#         next_croak_char_to_frog_list: defaultdict[Char, list[Frog]] = defaultdict(list)
#
#         for char in croakOfFrogs:
#             if len(next_croak_char_to_frog_list[char]) > 0:
#                 frog = next_croak_char_to_frog_list[char].pop()
#                 croaked = frog.croak_one_char(char)
#                 assert croaked
#                 next_croak_char_to_frog_list[frog.next_croak_char()].append(frog)
#             else:
#                 frog = Frog()
#                 croaked = frog.croak_one_char(char)
#                 if not croaked:
#                     return -1
#                 next_croak_char_to_frog_list[frog.next_croak_char()].append(frog)
#
#         min_n_frogs = 0
#
#         for char, frogs in next_croak_char_to_frog_list.items():
#             for frog in frogs:
#                 if not frog.can_mute():
#                     return -1
#                 min_n_frogs += 1
#
#         return min_n_frogs


# https://leetcode.cn/problems/minimum-number-of-frogs-croaking/solutions/2256739/shu-qing-wa-by-leetcode-solution-o532/comments/2009600

class Solution:
    def minNumberOfFrogs(self, croak_of_frogs: str) -> int:
        result = 0
        char_frequency: defaultdict[Char, int] = defaultdict(int)
        for char in croak_of_frogs:
            char_frequency[char] += 1
            if not (char_frequency['c'] >=
                    char_frequency['r'] >=
                    char_frequency['o'] >=
                    char_frequency['a'] >=
                    char_frequency['k']):
                return -1
            result = max(result, char_frequency['c'] - char_frequency['k'])
        if (char_frequency['c'] ==
                char_frequency['r'] ==
                char_frequency['o'] ==
                char_frequency['a'] ==
                char_frequency['k']):
            return result
        else:
            return -1
