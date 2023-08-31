from pkg.data_structure import ListNode


# https://leetcode.cn/problems/add-two-numbers
def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    l3: ListNode | None = None
    l3_last_node: ListNode | None = None
    l1_node_value: int = 0
    l2_node_value: int = 0
    add_one_at_higher_digit: bool = False
    while True:
        if l1 is None and l2 is None and add_one_at_higher_digit == 0:
            break
        if l1 is None:
            l1_node_value = 0
        else:
            l1_node_value = l1.val
            l1 = l1.next
        if l2 is None:
            l2_node_value = 0
        else:
            l2_node_value = l2.val
            l2 = l2.next
        sum_of_two_nodes = l1_node_value + l2_node_value + (1 if add_one_at_higher_digit else 0)
        if sum_of_two_nodes >= 10:
            sum_of_two_nodes -= 10
            add_one_at_higher_digit = True
        else:
            add_one_at_higher_digit = False
        l3_new_node = ListNode(val=sum_of_two_nodes)
        if l3 is None:
            l3 = l3_new_node
            l3_last_node = l3_new_node
        else:
            l3_last_node.next = l3_new_node
            l3_last_node = l3_new_node
    return l3
