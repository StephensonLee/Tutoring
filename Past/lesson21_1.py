class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printl(a):
    while (a!=None):
        print(a.val,end='!')
        a=a.next
    print()

def oddEvenList(head):
    if not head or not head.next: return head

    odd = head
    even = head.next
    evenHead = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
        printl(a)
    odd.next = evenHead
    return head

# Definition for singly-linked list.


a=ListNode(1)
a.next=ListNode(2)
a.next.next=ListNode(3)
a.next.next.next=ListNode(4)
a.next.next.next.next=ListNode(5)

printl(a)
oddEvenList(a)
printl(a)
# b=1pm
# while (1pm!=None):
#     print (1pm.val)
#     1pm=1pm.next



