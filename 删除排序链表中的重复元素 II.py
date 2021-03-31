# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #开始循环
        if head is None or head.next==None:
            return head
        else:
            #初始化指针指向
            before= head
            after = head.next
            pos = before
            while after.next!=None:
                #比较不相等后移
                if before.val != after.val:
                    before = after
                    after = after.next
                    if before.val != after.val:
                        pos = before
                else:
                    while after.val==before.val:
                        if after.next == None:
                            if pos.val == after.val:
                                head = None
                                return head
                            pos.next = None
                            return head
                        after = after.next
                    if after.next!=None:
                        if pos == before:
                            head = after
                            after = after.next
                            before = head
                            pos = before
                        else:
                            before = after 
                            after = after.next
                            if before.val != after.val:
                                pos.next = before
                                pos = before 
                    else:
                        if pos.val != before.val:
                            pos.next = after
                            return head
                        else:
                            pos = after
                            return pos
            if before.val == after.val and pos.val!=before.val:
                pos.next = None
                return head
            elif before.val == after.val and pos.val==before.val:
                head = None
                return head
            return head
if __name__ == '__main__':
    s = Solution()
    node_6 = ListNode(5)
    node_5 = ListNode(4,node_6)
    node_4 = ListNode(4,node_5)
    node_stick = ListNode(3)
    node_3 = ListNode(2,node_stick)
    node_2 = ListNode(1,node_3)
    node_1 = ListNode(1,node_2)
    head = ListNode()
    head = s.deleteDuplicates(head)
    p = head
    for i in range(2):
        print(p.val)
        p = p.next