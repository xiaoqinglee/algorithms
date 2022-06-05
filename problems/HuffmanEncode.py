# 霍夫曼树又称最优二叉树，是一种带权路径长度最短的二叉树。
# 所谓树的带权路径长度，就是树中所有的叶结点的权值乘上其到根结点的路径长度
# （若根结点为0层，叶结点到根结点的路径长度为叶结点的层数）。
# 树的路径长度是从树根到每一结点的路径长度之和，
# 记为WPL=（W1*L1+W2*L2+W3*L3+...+Wn*Ln），
# N个权值Wi（i=1,2,...n）构成一棵有N个叶结点的二叉树，
# 相应的叶结点的路径长度为Li（i=1,2,...n）。
# 可以证明霍夫曼树的WPL是最小的。

# https://github.com/dayu321/leetcode-6/blob/master/thinkings/run-length-encode-and-huffman-encode.md
# character 	frequency 	encoding
# a 	5 	1100
# b 	9 	1101
# c 	12 	100
# d 	13 	101
# e 	16 	111
# f 	45 	0

# 霍夫曼编码结果的bit数最少。

# 当霍夫曼树构造完毕的时候编码解码的映射关系就确定了，
# 编码：char -> bits, 等长 -> 不等长, 使用哈希就可以。
# 解码：bits -> char, 不等长 -> 等长, 使用霍夫曼树。

from pypkg.datatype import TreeNode


class HaffmanEncode:

    def __init__(self, char_to_frequency: dict[str, int]):

        if len(char_to_frequency) < 2:
            raise "待编码的字符个数小于2，编码无意义"

        # 这个工作交给堆比较合适
        def pop_node_with_min_v(list_: list[TreeNode]) -> TreeNode:
            min_v = min((node.val for node in list_))
            for i, node in enumerate(list_):
                if node.val == min_v:
                    return list_.pop(i)

        def build_tree(list_: list[TreeNode]) -> TreeNode:
            while len(list_) >= 2:
                node1 = pop_node_with_min_v(list_)
                node2 = pop_node_with_min_v(list_)
                # 这里 node1.val <= node2.val
                root: TreeNode = TreeNode(val=node1.val + node2.val, left=node1, right=node2)
                root.char = None  # 非叶子节点 char 值为非 None
                list_.append(root)
            return list_[0]

        def init_encoding_map(root: TreeNode) -> dict[str, list[int]]:
            temp: list[int] = []
            result: dict[str, list[int]] = {}

            def traverse(node: TreeNode) -> None:
                if node.char is not None:
                    result[node.char] = temp.copy()
                    return
                # haffman tree 中所有非叶子节点都有两个孩子
                temp.append(0)
                traverse(node.left)
                temp.pop()
                temp.append(1)
                traverse(node.right)
                temp.pop()

            traverse(root)
            return result

        node_list: list[TreeNode] = []
        for k, v in char_to_frequency.items():
            node: TreeNode = TreeNode(val=v, left=None, right=None)
            node.char = k  # 叶子结点 char 值为非 None
            node_list.append(node)

        self.__haffman_tree: TreeNode = build_tree(node_list)
        self.__encoding_map: dict[str, list[int]] = init_encoding_map(self.__haffman_tree)

    def encode(self, chars: str) -> list[int]:
        bits: list[int] = []
        for char in chars:
            bits_ = self.__encoding_map[char]
            bits.extend(bits_)
        return bits

    def decode(self, bits: list[int]) -> str:
        chars: list[str] = []
        node: TreeNode = self.__haffman_tree
        for bit in bits:
            if bit == 0:
                node = node.left
            elif bit == 1:
                node = node.right
            # 判断叶子结点
            if node.char is not None:
                chars.append(node.char)
                node = self.__haffman_tree
        return "".join(chars)


# character 	frequency 	encoding
# a 	5 	1100
# b 	9 	1101
# c 	12 	100
# d 	13 	101
# e 	16 	111
# f 	45 	0


if __name__ == '__main__':
    frequency_table = {
        "a": 5,
        "b": 9,
        "c": 12,
        "d": 13,
        "e": 16,
        "f": 45,
    }
    haffman: HaffmanEncode = HaffmanEncode(frequency_table)
    for char in frequency_table:
        print(haffman.encode(char))
    for char in frequency_table:
        print(haffman.decode(haffman.encode(char)))
    print(haffman.encode("abcdef"))
    print(haffman.decode([1, 1, 0, 0] +
                         [1, 1, 0, 1] +
                         [1, 0, 0] +
                         [1, 0, 1] +
                         [1, 1, 1] +
                         [0]))
