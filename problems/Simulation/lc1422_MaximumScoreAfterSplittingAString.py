class Solution:
    def maxScore(self, s: str) -> int:
        if len(s) < 2:
            raise 'invalid arg: "{}"'.format(s)
        score: int = (1 if s[0] == '0' else 0) + sum((1 for c in s[1:] if c == '1'))
        max_score: int = score
        for c in s[1:-1]:
            if c == '0':
                score += 1
            elif c == '1':
                score -= 1
            else:
                raise 'unexpected char: "{}"'.format(c)
            max_score = max(score, max_score)
        return max_score
