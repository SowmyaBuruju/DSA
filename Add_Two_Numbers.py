# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # Dummy node to simplify result list handling
        curr = dummy  # Pointer to track the last node in the result list
        carry = 0  # Initialize carry

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    dummy = ListNode()
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Helper function to convert a linked list back to a list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test Cases
l1 = list_to_linked_list([2, 4, 3])
l2 = list_to_linked_list([5, 6, 4])
result = Solution().addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [7, 0, 8]

l1 = list_to_linked_list([0])
l2 = list_to_linked_list([0])
result = Solution().addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [0]

l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = list_to_linked_list([9, 9, 9, 9])
result = Solution().addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]

l1 = list_to_linked_list([1, 8])
l2 = list_to_linked_list([0])
result = Solution().addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [1, 8]

l1 = list_to_linked_list([5])
l2 = list_to_linked_list([5])
result = Solution().addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [0, 1]
