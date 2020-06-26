from Linked_List import ListNode
from Linked_List import Linked_List
# 2 -> 4 -> 3,  5 -> 6 -> 7


def addTwoNumbers(l1, l2):
    temp1, temp2 = l1, l2
    flag = (temp1.val+temp2.val)//10
    head = ListNode((temp1.val+temp2.val) % 10)
    p = head
    temp1 = temp1.next
    temp2 = temp2.next
    while temp1 and temp2:
        p.next = ListNode((temp1.val+temp2.val+flag) % 10)
        flag = (temp1.val+temp2.val+flag)//10
        p = p.next
        temp1 = temp1.next
        temp2 = temp2.next

    while temp1:
        p.next = ListNode((temp1.val+flag) % 10)
        flag = (temp1.val+flag)//10
        p = p.next
        temp1 = temp1.next

    while temp2:
        p.next = ListNode((temp2.val+flag) % 10)
        flag = (temp2.val+flag)//10
        p = p.next
        temp2 = temp2.next

    if flag:
        p.next = ListNode(1)

    return head


if __name__ == "__main__":
    a = addTwoNumbers(Linked_List([2, 4, 3]).head, Linked_List([5, 6, 4]).head)
    print(Linked_List.HeadToLink(a))
