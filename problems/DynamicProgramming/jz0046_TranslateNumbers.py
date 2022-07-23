class Solution:
    def translateNum(self, num: int) -> int:
        num_str: str = str(num)

        def can_translate(number: str) -> bool:
            if len(number) == 1:
                return True
            elif len(number) == 2:
                if number[0] == "1" or (number[0] == "2" and 0 <= int(number) <= 25):
                    return True
                else:
                    return False
            else:
                return False

        # dp[i] 代表第i位索引上的数字作为字符串最后一个字符, [0...i]串的翻译方案个数
        # 题目所求答案为 dp[len()-1]
        dp: list[int | None] = [None] * len(num_str)

        for i in range(len(num_str)):
            if i == 0:
                dp[i] = 1 + 0
            elif i == 1:
                dp[i] = (dp[i-1] * 1) + (1 if can_translate(num_str[i-1:i+1]) else 0)
            else:
                dp[i] = (dp[i-1] * 1) + ((dp[i-2] * 1) if can_translate(num_str[i-1:i+1]) else 0)

        return dp[len(num_str)-1]
