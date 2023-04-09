# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        num1 = self.listnode_to_number(l1)
        num2 = self.listnode_to_number(l2)
        num_result = num1 + num2
        
        return self.number_to_linked_list(num_result)

    def listnode_to_number(self, ln):
        basamak = 0
        num_last = 0
        
        while ln != None:
            num = (10**basamak)*ln.val
            num_last = num_last + num
            ln = ln.next
            basamak += 1
            
        return num_last

    def number_to_linked_list(self, num):
        num_to_list = map(int, str(num))
        reversed_list = list(reversed(num_to_list))
        dummy = ListNode()
        head = dummy
        
        for i in reversed_list:
            head.next = ListNode(i)
            head = head.next
            i += 1
            
        return dummy.next
