from Linked_List import ListNode
from Linked_List import Linked_List

# merge two sorted linked lists

def mergeTwoLists(l1,l2):
    head = ListNode(0)
    p = head
    while l1 and l2:
        if l1.val > l2.val:
            p.next = ListNode(l2.val)
            l2 = l2.next
        else:
            p.next = ListNode(l1.val)
            l1 = l1.next
        p = p.next

    while l1:
        p.next = ListNode(l1.val)
        l1 = l1.next 
        p = p.next
    
    while l2:
        p.next = ListNode(l2.val)
        l2 = l2.next 
        p = p.next
    
    return head.next


# reverse linked list
def reverseList(head):
    if not head: return None
    cur = head 
    nxt = cur.next
    cur.next = None
    while nxt:
        nxt2 = nxt.next
        nxt.next = cur
        cur,nxt = nxt,nxt2
    return cur




if __name__ == "__main__":
    a = reverseList(Linked_List([1, 2, 4,7,5,3]).head)
    print(Linked_List.HeadToLink(a))