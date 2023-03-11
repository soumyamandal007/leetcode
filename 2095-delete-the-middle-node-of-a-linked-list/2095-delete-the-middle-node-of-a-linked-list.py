# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        itr = head
        count = 0
        while itr:
            count += 1
            itr =  itr.next
        print(count)
        del_node = count // 2
        slow = head
        n = 0
        while slow:
            if n == del_node - 1:
                slow.next = slow.next.next
            n += 1
            slow = slow.next
        return head