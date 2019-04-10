'''
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def hasCycle(head):
    slow=head
    fast=head
    while(fast != None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
        if slow == fast:
            return True
    return False

