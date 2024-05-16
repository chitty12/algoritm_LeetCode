from typing import Optional

from networkx import is_empty


class ListNode:
    def __init__(self, val = 0, next = None) :
        self.val = val
        self.next = next

    def settingNode(self, headList):
        head = ListNode(headList[0])

        current = head

        for val in headList[1:]:
            current.next = ListNode(val)
            current = current.next
            
            return head
        

class LinkedList:
    def __init__(self) :
        self.head = None
        self.tail = None
        self.length = 0
    
    def is_empty(self):
        return self.length == 0

    def prepend(self, val):
        new_node = ListNode(val)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def append(self, val):
        new_node = ListNode(val)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail
            self.tail = new_node
        self.length += 1





class Solution :
    def getComponents(self, head: Optional[ListNode], nums):
        count = 0
        while head:
            if head.val in nums: 
                if head.val in nums:
                    if head.next is None or head.next.val not in nums :
                        count += 1
                    head = head.next
        return count
    

head_list = [0, 1, 2, 3, 4]
nums = [0, 3, 1, 4]


head = ListNode()
nodeList = head.settingNode(head_list)
solution = Solution()
print(nodeList)
result = solution.getComponents(nodeList, nums)

print(result)

