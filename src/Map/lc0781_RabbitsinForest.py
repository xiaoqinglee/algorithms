import math


# https://leetcode.cn/problems/rabbits-in-forest
class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        # 把 answer 变为"加上自己有多少个兔子"
        for nth_rabbit in range(len(answers)):
            answers[nth_rabbit] += 1

        answer_to_n_rabbits_say_that_answer: dict[int, int] = {}
        for answer in answers:
            if answer not in answer_to_n_rabbits_say_that_answer:
                answer_to_n_rabbits_say_that_answer[answer] = 1
            else:
                answer_to_n_rabbits_say_that_answer[answer] += 1

        # 有1个兔子说和自己毛色相同的加上自己一共有3个兔子, 那么最少有3个兔子. 3 * (1)
        # 有3个兔子说和自己毛色相同的加上自己一共有3个兔子, 那么最少有3个兔子. 3 * (1)
        # 有4个兔子说和自己毛色相同的加上自己一共有3个兔子, 那么最少有3+3个兔子. 3 * (1+1)
        # 有5个兔子说和自己毛色相同的加上自己一共有3个兔子, 那么最少有3+3个兔子. 3 * (1+1)
        # 有6个兔子说和自己毛色相同的加上自己一共有3个兔子, 那么最少有3+3个兔子. 3 * (1+1)
        # 有7个兔子说和自己毛色相同的加上自己一共有3个兔子, 那么最少有3+3+3个兔子. 3 * (1+1+1)

        return sum((answer * math.ceil(n / answer) for answer, n in answer_to_n_rabbits_say_that_answer.items()))
