# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head is not None:
            n = head.next
            head.next = prev
            prev = head
            head = n
        return prev

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)

l1.next = l2
l2.next = l3

result = l1

while result.next is not None:
    print(result.val)
    result = result.next
print(result.val)

print "Reversing linked list..."

s = Solution()
result = s.reverseList(l1)

while result.next is not None:
    print(result.val)
    result = result.next
print(result.val)
