# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        curr = head

        while list1 != None or list2 != None:
            
            num1,num2 = None,None
            
            if list1:
                num1 = list1.val
            
            if list2:
                num2 = list2.val
                
            if list1 and list2:
                if num1 < num2:
                    curr.next = list1
                    curr = list1
                    list1 = list1.next
                    
                else:
                    curr.next = list2
                    curr = list2
                    list2 = list2.next
                    
            elif list1:
                curr.next = list1
                curr = list1
                list1 = list1.next
            
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        
        return head.next
                
        