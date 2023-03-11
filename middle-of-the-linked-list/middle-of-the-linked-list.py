# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lenlist = 0
        itr = node = head 
        while itr:
            lenlist += 1
            itr = itr.next
        print(lenlist)
        if lenlist % 2 == 0:
            index = lenlist // 2 + 1
        else:
            index = (lenlist + 1) // 2
        print(index)
        count = 0
        while node:
            if count == index-1:
                return node
            else:
                node = node.next
                count += 1
        



