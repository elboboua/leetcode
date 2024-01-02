class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        new_head = None
        temp = head
        while temp is not None:
            new_node = ListNode(temp.val, new_head)
            new_head = new_node
            temp = temp.next 

        return new_head
    
sol = Solution()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head = sol.reverseList(head)
assert new_head.val == 5
assert new_head.next.val == 4
assert new_head.next.next.val == 3
assert new_head.next.next.next.val == 2
assert new_head.next.next.next.next.val == 1

head = ListNode(1, ListNode(2))
new_head = sol.reverseList(head)
assert new_head.val == 2
assert new_head.next.val == 1

print("Passed")