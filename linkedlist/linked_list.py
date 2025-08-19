class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

    def __str__(self):
        return f'{self.val} -> {self.next.__str__()}'
    
    def __repr__(self):
        return f'{self.val} -> {self.next.__repr__()}'


def link(array: list):
    # Create a linked-list from an array

    def link_helper(index: int):
        if index == len(array):
            return None
        
        else:
            node = ListNode(array[index])
            node.next = link_helper(index + 1)

            return node
        
    return link_helper(0)