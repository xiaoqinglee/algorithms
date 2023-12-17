import bisect


IntervalVal = tuple[int, int]  # 左闭右闭区间


class IntervalTreeNode:
    def __init__(self, interval_left: int):
        self.interval_left: int = interval_left
        self.interval_right_s: list[int] = []  # li[len()-1]放最大的元素
        self.interval_right_max: int = -float("inf")
        self.left: AugmentedIntervalTree = AugmentedIntervalTree()
        self.right: AugmentedIntervalTree = AugmentedIntervalTree()


class AugmentedIntervalTree:
    def __init__(self, root: IntervalTreeNode | None = None):
        self.root: IntervalTreeNode | None = root

    def add_interval(self, interval: IntervalVal) -> int:
        interval_l, interval_r = interval
        assert interval_l <= interval_r
        if self.root is None:
            self.root = IntervalTreeNode(interval_left=interval_l)
        if interval_l == self.root.interval_left:
            bisect.insort(self.root.interval_right_s, interval_r)
            self.root.interval_right_max = max(self.root.interval_right_max, interval_r)
            return self.root.interval_right_max
        if interval_l < self.root.interval_left:
            subtree_interval_right_max = self.root.left.add_interval(interval)
        else:
            subtree_interval_right_max = self.root.right.add_interval(interval)
        self.root.interval_right_max = max(self.root.interval_right_max, subtree_interval_right_max)
        return self.root.interval_right_max

    def get_overlapping_intervals(self, interval: IntervalVal) -> list[IntervalVal]:
        interval_l, interval_r = interval
        assert interval_l <= interval_r
        if self.root is None:
            return []

        # test root
        overlapping_intervals: list[IntervalVal] = []
        if interval_l > self.root.interval_right_max:
            # do nothing
            pass
        else:
            for self_interval_right in self.root.interval_right_s:
                if not (interval_r < self.root.interval_left or interval_l > self_interval_right):
                    overlapping_intervals.append((self.root.interval_left, self_interval_right))

        # test left child
        left_hand_side: list[IntervalVal] = self.root.left.get_overlapping_intervals(interval)

        # test right child
        right_hand_side: list[IntervalVal] = []
        if interval_r < self.root.interval_left:
            # do nothing
            pass
        else:
            right_hand_side = self.root.right.get_overlapping_intervals(interval)

        return left_hand_side + overlapping_intervals + right_hand_side


# https://en.wikipedia.org/wiki/Interval_tree#Augmented_tree
# When searching the trees for nodes overlapping with a given interval, you can immediately skip:
#
#     all nodes to the right of nodes whose low value is past the end of the given interval.
#     all nodes that have their maximum high value below the start of the given interval.
#
#
# 一棵树的三个字段:
#     (this interval left, this interval right), whole tree max right
# 有性质:
#     this interval left > left subtree max left
#     this interval left < right subtree min left
# 所以：
#     target interval left > whole tree max right => 没必要check whole tree 了
#     target interval right < right subtree min left => 没必要check right subtree 了


# http://www.mit.edu/~6.005/sp11/psets/ps2/assignment.html
#
# Part C: Augmented Binary Search Trees [35 points]
#
# For this problem, only modify the source code provided in the ps2.bst_augmented_abstract package.
#
# So far, we have described and implemented Binary Search Trees with no special properties:
# nodes were simply sorted and arranged by key values.
#
# Now, we will extend the functionality of our Binary Search Trees to create Augmented Search Trees.
# Augmented Search Trees are special types of Binary Search Trees
# that, apart from maintaining a sorted order of elements (based on their keys),
# also track some information about elements based on where these elements are stored in Binary Search Trees.
# We provide an abstract class for augmented search trees in AugmentedBinarySearchTree.java.
#
# Augmented Binary Search trees have numerous applications, but we will focus on a few simple examples.
# For this part, you will encounter three different Augmented Binary Search trees:
#
#     An augmented search tree that stores the number of descendants below each node.
#     An augmented search tree that stores the sum of the keys of all leaves below each node.
#     An augmented search tree that stores the range of node values below each node.
#
# The first augmented search tree simply stores, at each node, the number
# of descendant nodes below it (excluding the node itself).
# This information must be dynamically updated during insertion and deletion of elements from the Binary Search Tree,
# without needing to visit all of the elements in the tree.
# A working implementation of this augmented tree is provided to you in NumberDescendantsBinarySearchTree.java.
# This implementation uses code from the AugmentedBinarySearchTree class, and is thus surprisingly simple.
#
# The second augmented tree stores, at each node, the sum
# of the keys of all descendant leaves below it (excluding the node itself).
# A leaf node is defined as a node that has no descendant nodes.
# Note that a tree with a single node should have an augmented value of 0,
# since the node has no descendant leaves.
# This information must again be dynamically updated during insertion and deletion of elements as before,
# without having to visit all the elements in the tree.
# It will be your job to fill in code for this augmentation in LeafSumBinarySearchTree.java.
#
# The third and final augmented tree stores, at each node, the range
# of values stored in the subtree containing the node (that is the difference between the max and min values).
# Again, this information must be dynamically updated during insertion and deletion of elements,
# without having to visit all the elements in the tree.
# Note that in this case we have given you
# a new class to work with, RangeBinaryNode.java, which
# in addition to the augmented value (representing the range) stores the value
# of the minimum and maximum elements in the tree.
# It will be your job to fill in code for this augmentation in RangeBinarySearchTree.java
# to update the augmented value (range), along with the minimum and maximum.
