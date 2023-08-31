from collections import deque


# https://leetcode.cn/problems/word-ladder
class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: list[str]) -> int:
        if end_word not in word_list:
            return 0

        # 修整参数
        end_word_index = word_list.index(end_word)
        word_list = word_list[:end_word_index] + word_list[end_word_index+1:]
        if begin_word in word_list:
            begin_word_index = word_list.index(begin_word)
            word_list = word_list[:begin_word_index] + word_list[begin_word_index+1:]
        word_list = [begin_word] + word_list + [end_word]

        # 建立邻接矩阵
        matrix: list[list[bool]] = [[False] * len(word_list) for _ in range(len(word_list))]

        def init_matrix() -> None:

            def has_edge(string1: str, string2: str) -> bool:
                if string1 == string2:
                    raise "Unexpected Input"
                if len(string1) != len(string2):
                    return False
                for i in range(len(string1)):
                    if string1[:i] == string2[:i] and string1[i+1:] == string2[i+1:]:
                        return True
                return False

            for i in range(len(word_list)):
                for j in range(i+1, len(word_list)):
                    if has_edge(word_list[i], word_list[j]):
                        matrix[i][j] = True
                        matrix[j][i] = True

        init_matrix()
        FRONT_TO_BACK: int = 0
        BACK_TO_FRONT: int = 1

        queue: list[deque[tuple[int, int]]] = [deque(), deque()]
        solved_vs: list[set[int]] = [set(), set()]
        prev_v: list[list[int | None]] = [[None] * len(word_list), [None] * len(word_list)]

        queue[FRONT_TO_BACK].append((0, -1))
        queue[BACK_TO_FRONT].append((len(word_list)-1, -1))

        joining_v: int | None = None
        direction: int = FRONT_TO_BACK
        other_direction: int = BACK_TO_FRONT

        # 有交集前不能停.
        # 一个queue为空说明它已经访问了所有和它邻接的节点, 它在与世隔绝的孤岛上, 所以连接起点和终点的路径不存在.
        while (len(solved_vs[FRONT_TO_BACK]) + len(solved_vs[BACK_TO_FRONT]) <= len(word_list)
               and not (len(queue[FRONT_TO_BACK]) == 0 or len(queue[BACK_TO_FRONT]) == 0)):

            v_pair_count = len(queue[direction])
            for i in range(v_pair_count):
                v, prev = queue[direction].popleft()
                if v in solved_vs[direction]:  # 只在此处判断该v是否已经被访问过
                    continue

                solved_vs[direction].add(v)
                prev_v[direction][v] = prev

                if v in solved_vs[other_direction]:
                    joining_v = v
                    break

                for adj_v in [v for v, is_adj in enumerate(matrix[v]) if is_adj is True]:  # 这里就不判断该v是否被访问过了
                    queue[direction].append((adj_v, v))

            if joining_v is not None:
                break
            direction, other_direction = other_direction, direction

        if joining_v is None:
            return 0

        sequence: deque[str] = deque()

        v = joining_v
        while word_list[v] != begin_word:
            sequence.appendleft(word_list[v])
            v = prev_v[FRONT_TO_BACK][v]
        sequence.appendleft(word_list[v])
        sequence.pop()

        v = joining_v
        while word_list[v] != end_word:
            sequence.append(word_list[v])
            v = prev_v[BACK_TO_FRONT][v]
        sequence.append(word_list[v])

        print(sequence)
        return len(sequence)
