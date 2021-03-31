class ListNode(object):
    def __init__(self,val = 0,next = None):
        self.val = val 
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        node = ListNode(0)
        node = head
        count = 1
        #算出总节点数
        while node.next != None:
            count = count+1
            node = node.next
        node = head 
        #找到left和right节点
        a = []
        b = []
        for i in range(count):
            if i >= (left-1) and i<=(right-1):
                a.append(node.val)
            node = node.next
        for i in range(right-left,-1,-1):
            b.append(a[i])
        node = head
        pos = 0
        for i in range(count):
            if i >= (left-1) and i<=(right-1):
                node.val = b[pos]
                pos = pos+1
            node = node.next
        return head
# if __name__ == '__main__':  
#     L3 = ListNode(4)
#     L2 = ListNode(3,L3)
#     L1 = ListNode(2,L2)
#     head = ListNode(1,L1)
#     s = Solution()
#     head = s.reverseBetween(head,1,4)
#     for i in range(4):
#         print(head.val)
#         head = head.next