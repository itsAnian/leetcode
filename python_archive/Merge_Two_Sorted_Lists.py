from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        firstNode = mergedList
        while(list1 or list2):
            if list1 and not list2:
                firstNode.next = ListNode(list1.val)
                firstNode = firstNode.next
                list1 = list1.next
            elif (not list1 and list2):
                firstNode.next = ListNode(list2.val)
                firstNode = firstNode.next
                list2 = list2.next
            elif (list1.val == list2.val or list1.val < list2.val):
                firstNode.next = ListNode(list1.val)
                firstNode = firstNode.next
                list1 = list1.next
            else:
                firstNode.next = ListNode(list2.val)
                firstNode = firstNode.next
                list2 = list2.next

        return mergedList.next
        
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])
sol = Solution()
print(sol.mergeTwoLists(list1, list2))
