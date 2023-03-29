# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        senti = ListNode(0) #creting a sentinal head so that we can return empty lists
        senti.next = head
        prev = senti
        itr = head
        while itr:
            if itr.val == val:
                prev.next = itr.next
            else:
                prev = itr
            itr = itr.next
        return senti.next
