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


if __name__ == "__main__":
    from basics.sort.data_structure_based_sort.heap_sort import heap_sort
    from basics.sort.data_structure_based_sort.skiplist_sort import skiplist_sort

    nums = [1, 1, 1, 1, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
            57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
            84, 85, 90, 90, 90, 90, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108,
            109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
            130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150,
            151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171,
            172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192,
            193, 194, 195, 200, 200, 200, 200, 200]
    import random

    random.shuffle(nums)
    s1 = heap_sort(nums.copy())

    import random

    random.shuffle(nums)
    s2 = bst_sort(nums.copy())

    import random

    random.shuffle(nums)
    s3 = skiplist_sort(nums.copy())

    print(len(s1), len(s2), len(s3))
    print(s1 == s2 == s3)
    print(id(s1) == id(s2))
    print(id(s1) == id(s2))
    print(id(s2) == id(s3))
