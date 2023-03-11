# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        count = 0
        itr = head
        fast = head
        slow = head
        while itr:
            count += 1
            itr = itr.next
        print(count)
        for _ in range(count//2):
            print(fast.val)
            fast = fast.next
        left = []
        right = []
        while slow and fast:
            print(slow.val,fast.val)
            left.append(slow.val)
            right.append(fast.val)
            slow = slow.next
            fast = fast.next
        print(left,right)
        ans = -1
        for i in range(len(left)):
            summ = left[i] + right[-1-i]
            print(summ)
            ans = max(ans,summ)
        return ans





        
