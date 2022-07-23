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

        # dp[i][0] 代表第i位索引上的数字作为字符串最后一个字符, 且该数字单独翻译时[0...i]串的翻译方案个数
        # dp[i][1] 代表第i位索引上的数字作为字符串最后一个字符, 且该数字和其前一位合并翻译时[0...i]串的翻译方案个数, 可能为零
        # 题目所求答案为 dp[len()-1][0] + dp[len()-1][1]
        dp: list[list[int | None]] = [[None, None] for _ in range(len(num_str))]

        for i in range(len(num_str)):
            if i == 0:
                dp[i][0] = 1
                dp[i][1] = 0
            elif i == 1:
                dp[i][0] = (dp[i-1][0] + dp[i-1][1]) * 1
                dp[i][1] = 1 if can_translate(num_str[i-1:i+1]) else 0
            else:
                dp[i][0] = (dp[i-1][0] + dp[i-1][1]) * 1
                dp[i][1] = ((dp[i-2][0] + dp[i-2][1]) * 1) if can_translate(num_str[i-1:i+1]) else 0

        return dp[len(num_str)-1][0] + dp[len(num_str)-1][1]
