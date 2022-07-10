from pkg.data_structure import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rob(self, root: TreeNode | None) -> int:

        # key: tuple[tree, tree_root_was_robbed]
        # value: max_value_you_can_rob_from_this_tree
        max_value_cache: dict[tuple[TreeNode | None, bool]] = {
            (None, False): 0,
            (None, True): 0,
        }

        def fill_max_value_cache(tree: TreeNode | None) -> None:
            if tree is None:
                return

            fill_max_value_cache(tree.left)
            fill_max_value_cache(tree.right)

            # rob tree root
            value_when_rob_tree_root = (tree.val +
                                        max_value_cache[(tree.left, False)] +
                                        max_value_cache[(tree.right, False)])
            # not rob tree root
            value_when_not_rob_tree_root = (0 +
                                            max(max_value_cache[(tree.left, False)],
                                                max_value_cache[(tree.left, True)]) +
                                            max(max_value_cache[(tree.right, False)],
                                                max_value_cache[(tree.right, True)]))
            max_value_cache[(tree, True)] = value_when_rob_tree_root
            max_value_cache[(tree, False)] = value_when_not_rob_tree_root

        fill_max_value_cache(root)
        return max(max_value_cache[(root, True)], max_value_cache[(root, False)])
