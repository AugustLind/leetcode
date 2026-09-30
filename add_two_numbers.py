# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:

        num_1 = self.find_number(l1)
        num_2 = self.find_number(l2)

        sum = num_1 + num_2

        dummy = ListNode(0)
        curr = dummy

        if sum == 0:
            return ListNode(0)

        while sum > 0:
            digit = sum % 10
            curr.next = ListNode(digit)
            curr = curr.next
            sum = sum // 10

        return dummy.next

    def find_number(self, ln: ListNode) -> int:
        num = 0
        denom = 0

        while True:
            num += ln.val * 10**denom
            denom += 1
            if ln.next == None:
                break

            ln = ln.next

        return num
