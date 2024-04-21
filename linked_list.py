# is_empty(): O(1)
# prepend(): O(n)
# append(): O(n) (조건부 O(1))
# set_head(index): O(1)
# access(index): O(1)
# insert(item, index): O(n)
# remove(index): O(n)
from typing import Optional


class ListNode :
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
    


class Solution :
    # Optional : typing 모듈에서 제공하는 타입, None 또는 Listnode값을 가짐
    def getComponents(self, head: Optional[ListNode], nums):
        count = 0
        # for는 'iterable'을 순회하므로 적절하지 않음.
        # while은 연속된 노드를 하나씩 순회하면서 확인함.
        while head:
            if head.val in nums:
                if head.next is None or head.next.val not in nums:                    
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


                




