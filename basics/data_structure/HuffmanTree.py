import heapq
from pkg.data_structure import TreeNode


Char = str
Bit = int


class HuffmanCoding:

    def __init__(self, char_to_frequency: dict[Char, int]):

        def build_tree(char_to_frequency: dict[Char, int]) -> TreeNode:
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

        def init_encoding_map(root: TreeNode) -> dict[Char, list[Bit]]:
            temp: list[Bit] = []
            result: dict[Char, list[Bit]] = {}

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
        self.__encoding_map: dict[Char, list[Bit]] = init_encoding_map(self.__huffman_tree)

    def encode(self, chars: str) -> list[Bit]:
        bits: list[Bit] = []
        for char in chars:
            bits_ = self.__encoding_map[char]
            bits.extend(bits_)
        return bits

    def decode(self, bits: list[Bit]) -> str:
        chars: list[Char] = []
        node: TreeNode = self.__huffman_tree
        for bit in bits:
            if bit == 0:
                node = node.left
            else:  # bit == 1
                node = node.right
            # 判断叶子结点
            if node.char is not None:
                chars.append(node.char)
                node = self.__huffman_tree
        return "".join(chars)


# 霍夫曼树是带权路径长度最短二叉树。

# 设二叉树具有N个带权叶结点，从根结点到各叶结点的路径长度与相应叶节点权值的乘积之和
# 称为树的带权路径长度（Weighted Path Length of Tree，WPL）。
# WPL=（W1*L1+W2*L2+W3*L3+...+Wn*Ln）
# 可以证明霍夫曼树的WPL是最小的。

# 霍夫曼树元素的查找总是在叶子节点结束， 就像 B Plus 树元素key的查找总在叶子节点结束一样。
# 叶子节点的权重是叶子节点被查询的概率， 霍夫曼树WPL最小所以一个正确构建的霍夫曼树在解码过程中平均查找高度最小。

# 霍夫曼编码结果的bit数最少。

# 当霍夫曼树构造完毕的时候编码解码的映射关系就确定了，
# 编码：char -> bits, 等长 -> 不等长, 使用哈希就可以。
# 解码：bits -> char, 不等长 -> 等长, 使用霍夫曼树。

# # 霍夫曼树和平衡搜索树的不同之处：
#
#     霍夫曼树上叶子节点被访问的概率不相同
#     平衡搜索树叶子节点和非叶子节点被访问的概率相同
#
#     霍夫曼树的意图是叶子节点权重和最小
#     平衡搜索树的意图是各个路径高度均匀, 从而降低总高度
#
#     霍夫曼树搜索动作仅仅在叶子节点停下来
#     平衡搜索树搜索动作可能在叶节点停下来，可能在非叶子节点停下来
#
#     霍夫曼树创建树的过程要创建新节点
#     平衡搜索树（如avl rb treap）建树过程不创建新节点


# https://github.com/dayu321/leetcode-6/blob/master/thinkings/run-length-encode-and-huffman-encode.md
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
