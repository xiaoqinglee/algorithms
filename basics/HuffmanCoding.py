# 霍夫曼树又称最优二叉树，是一种带权路径长度最短的二叉树。
# 所谓树的带权路径长度，就是树中所有的叶结点的权值乘上其到根结点的路径长度
# （若根结点为0层，叶结点到根结点的路径长度为叶结点的层数）。
# 树的路径长度是从树根到每一结点的路径长度之和，
# 记为WPL=（W1*L1+W2*L2+W3*L3+...+Wn*Ln），
# N个权值Wi（i=1,2,...n）构成一棵有N个叶结点的二叉树，
# 相应的叶结点的路径长度为Li（i=1,2,...n）。
# 可以证明霍夫曼树的WPL是最小的。

# 霍夫曼树元素的查找总是在叶子节点结束， 就像 B Plus 树元素value的查找总在叶子节点结束一样。
# 叶子节点的权重是叶子节点被查询的概率， 霍夫曼树WPL最小所以一个正确构建的霍夫曼树在解码过程中平均查找高度最小。

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


import heapq
from pkg.data_structure import TreeNode


class HuffmanCoding:

    def __init__(self, char_to_frequency: dict[str, int]):

        def build_tree(char_to_frequency: dict[str, int]) -> TreeNode:
            if len(char_to_frequency) < 2:
                raise "待编码的字符小于2， 没有编码意义"

            node_list: list[TreeNode] = []
            for char, frequency in char_to_frequency.items():
                node: TreeNode = TreeNode(val=frequency, left=None, right=None)
                node.char = char  # 叶子结点 char 值为非 None
                node_list.append(node)

            # heap value: tuple(frequency, node_index_in_original_list)
            min_heap: list[tuple[int, int]] = [(node.val, i) for i, node in enumerate(node_list)]
            heapq.heapify(min_heap)
            while len(min_heap) >= 2:
                _, min1_index = heapq.heappop(min_heap)
                _, min2_index = heapq.heappop(min_heap)
                # 这里 min1.val <= min2.val
                node: TreeNode = TreeNode(val=node_list[min1_index].val + node_list[min2_index].val,
                                          left=node_list[min1_index],
                                          right=node_list[min2_index])
                node.char = None  # 非叶子节点 char 值为 None
                node_list.append(node)
                heapq.heappush(min_heap, (node.val, len(node_list)-1))

            root: TreeNode = node_list[-1]
            return root

        def init_encoding_map(root: TreeNode) -> dict[str, list[int]]:
            temp: list[int] = []
            result: dict[str, list[int]] = {}

            def traverse(node: TreeNode) -> None:
                if node.char is not None:
                    result[node.char] = temp.copy()
                    return
                # huffman tree 中所有非叶子节点都有两个孩子
                temp.append(0)
                traverse(node.left)
                temp.pop()
                temp.append(1)
                traverse(node.right)
                temp.pop()

            traverse(root)
            return result

        self.__huffman_tree: TreeNode = build_tree(char_to_frequency)
        self.__encoding_map: dict[str, list[int]] = init_encoding_map(self.__huffman_tree)

    def encode(self, chars: str) -> list[int]:
        bits: list[int] = []
        for char in chars:
            bits_ = self.__encoding_map[char]
            bits.extend(bits_)
        return bits

    def decode(self, bits: list[int]) -> str:
        chars: list[str] = []
        node: TreeNode = self.__huffman_tree
        for bit in bits:
            if bit == 0:
                node = node.left
            elif bit == 1:
                node = node.right
            # 判断叶子结点
            if node.char is not None:
                chars.append(node.char)
                node = self.__huffman_tree
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
    huffman: HuffmanCoding = HuffmanCoding(frequency_table)
    for char in frequency_table:
        print(huffman.encode(char))
    for char in frequency_table:
        print(huffman.decode(huffman.encode(char)))
    print(huffman.encode("abcdef"))
    print(huffman.decode([1, 1, 0, 0] +
                         [1, 1, 0, 1] +
                         [1, 0, 0] +
                         [1, 0, 1] +
                         [1, 1, 1] +
                         [0]))
