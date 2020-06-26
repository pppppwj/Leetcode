# def singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Linked_List:
    head = None

    def __init__(self, nums):
        if nums:
            self.head = ListNode(nums[0])
            temp = self.head
            for i in range(1, len(nums)):
                temp.next = ListNode(nums[i])
                temp = temp.next

    @classmethod
    def HeadToLink(cls, h):
        nums = []
        while h:
            nums.append(h.val)
            h = h.next
        return cls(nums)

    def __str__(self):
        res = ""
        temp = self.head
        while(temp):
            res += str(temp.val) + ','
            temp = temp.next
        res = '[' + res[:-1] + ']'
        return res