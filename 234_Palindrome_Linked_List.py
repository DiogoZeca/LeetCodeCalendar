# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        prev = None
        while slow:
            nextTemp = slow.next
            slow.next = prev
            prev = slow
            slow = nextTemp
        
        # Compare the first and second half of the linked list
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True

