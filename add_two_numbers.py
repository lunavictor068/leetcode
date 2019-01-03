'''
Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        current_node = ListNode(0)
        # store reference to head
        head = current_node
        # loop until both lists are done
        while True:
        	l1_val = 0
        	l2_val = 0
        	if l1:
        		l1_val = l1.val
        	if l2:
        		l2_val = l2.val
        	# add leading 0 to addition of values. Indicates a carry of 0 on single digit numbers
        	add_str = str(0) + str(l1_val + l2_val + carry)
        	carry = int(add_str[-2])
        	val = int(add_str[-1])
        	current_node.val = val
        	# stop when there are no more values and no carry
        	if any([n.next for n in filter(None, [l1, l2])]) or carry != 0:
        		# update references for next iteration
        		current_node.next = ListNode(0)
        		current_node = current_node.next
        		if l1:
        			l1 = l1.next
        		if l2:
        			l2 = l2.next
        	else:
        		break
        return head
