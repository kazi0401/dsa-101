from linked_list import *

def reverseBetween(head, left, right):

    # points to the head
    # makes cases like [5] easier
    dummy = ListNode(-1, head)

    # figure out when to start reversing
    prev, curr = dummy, head
    i = 1
    while i < left:
        prev, curr = curr, curr.next 
        i += 1


    # save the prev and curr in variables
    # so we can adjust these pointers later
    temp1, revTail = prev, curr 
    # reverse sequence
    while i <= right:
        temp = curr.next 

        curr.next = prev 

        prev, curr = curr, temp 
        i += 1
    
    # adjusting pointers
    temp1.next = prev
    revTail.next = curr

    return dummy.next

if __name__ == '__main__':
    head = link([5])
    reverseBetween(head, 1, 1)