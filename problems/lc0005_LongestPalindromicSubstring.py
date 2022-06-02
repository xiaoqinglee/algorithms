def longest_palindrome(s: str) -> str:
    if len(s) == 0:
        return s

    # dp[][]是个行列都为len(s)的正方形数组,
    # 如果 s[i:j+1]是回文，那么dp[i][j] == True
    # 否则dp[i][j] == False。
    # 我们需要填充数组的右上角，因为 0<=i<=j<len(s)
    dp: list[list[bool | None]] = [[None] * len(s) for i in range(len(s))]
    longest_palindrome_substring: str = ''
    longest_palindrome_substring_length: int = 0

    def populate_dp_table():
        substring_length = 0
        while True:
            substring_length += 1
            if substring_length > len(s):
                break
            for i in range(len(s)):
                j = i + (substring_length - 1)
                if j >= len(s):
                    break
                if j - i == 0:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                # 顺便记录（答案不唯一，也即存在两个不同回文子串长度相同的情景，保留任意一个即可）
                nonlocal longest_palindrome_substring_length
                nonlocal longest_palindrome_substring
                if dp[i][j] and substring_length > longest_palindrome_substring_length:
                    longest_palindrome_substring_length = substring_length
                    longest_palindrome_substring = s[i:j+1]

    populate_dp_table()
    return longest_palindrome_substring
