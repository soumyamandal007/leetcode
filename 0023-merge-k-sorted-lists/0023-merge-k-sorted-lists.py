# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = curr = ListNode(-1)
        node = []
        for l in lists:
            curr_head = l
            while curr_head:
                node.append(curr_head.val)
                curr_head = curr_head.next
        print(node)
        for i in sorted(node):
            curr.next = ListNode(i)
            curr = curr.next
        return head.next
        