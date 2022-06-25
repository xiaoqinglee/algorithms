def bst_sort(nums: list[int]) -> list[int]:
    # # 应对 leetcode极端测试用例: 升序超大数组
    # import random
    # random.shuffle(nums)

    if len(nums) == 0:
        return nums

    sorted_ = []
    from basics.data_structure.BST import BST
    bst: BST | None = None
    for num in nums:
        if bst is None:
            bst = BST(key=num, val=1)
        else:
            count: int | None = bst.search(key=num)
            if count is None:
                bst.insert(key=num, val=1)
            else:
                bst.insert(key=num, val=count + 1)

    def traverse(root: BST | None) -> None:
        if root is None:
            return
        traverse(root.left)
        for i in range(root.val):
            sorted_.append(root.key)
        traverse(root.right)

    traverse(bst)

    return sorted_
