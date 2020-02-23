class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

    示例：
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp = ListNode(0)
        root = tmp
        carry = 0
        while l1 or l2 or carry:
            tmp.next = ListNode(0)
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if carry:
                val += carry
                carry = 0
            if val >= 10:
                val -= 10
                carry = 1
            tmp.next.val = val
            tmp = tmp.next
        return root.next