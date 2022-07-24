class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # 矩形以列表 [x1, y1, x2, y2] 的形式表示，(x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标
        # 只在角或边接触的两个矩形不构成重叠
        return (abs((rec1[0] + rec1[2]) / 2 - (rec2[0] + rec2[2]) / 2) <
                ((rec1[2] - rec1[0]) / 2 + (rec2[2] - rec2[0]) / 2)
                and
                abs((rec1[1] + rec1[3]) / 2 - (rec2[1] + rec2[3]) / 2) <
                ((rec1[3] - rec1[1]) / 2 + (rec2[3] - rec2[1]) / 2))
