# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        number = 0
        rev = ''
        itr = head
        flag = 1
        while itr.next:
            number += flag*itr.val
            flag *= 10
            rev += str(itr.val)
            #print(itr.val)
            itr = itr.next
            #print(number,flag)
        number += flag*itr.val
        rev += str(itr.val)
        print(number)
        print(rev)
        if number == int(rev):
            return True
