
class Node:
    def __init__(self, val = None, next = None):
        self.val, self.next = val, next


class LinkedList:
    def __init__(self):
        self.head: Node = None
    

    def insert(self, value):
        '''
        Insert the node at the head of the linked list

            Ex. 
                4 -> 3 -> 7
                insert(1)
                1 -> 4 -> 3 -> 7
        '''
    

    def delete(self, value):
        '''
        Remove the node that contains the given value
            Ex.
                1 -> 2 -> 3
                remove(2)
                1 -> 3
        
        Do nothing if the value does not exist. 
        Assume no duplicates
            
        '''


    def length(self):
        ''' 
        Compute the length of the linked list 
            Ex.
                1 -> 2 -> 3
                    returns 3
    
        '''
        pass 

    def search(self, target):
        ''' 
        Returns the position of the node where node.value == target.
        Return -1 otherwise

            Ex. 
                4 -> 1 -> 10 -> 8
                    Target = 8
                    Returns 4
                3 -> 2 -> 5
                    Target = 4
                    Returns -1
        '''
    
    def __str__(self):
        ''' 
        Traverse the linked list and print the value of each node!
            Ex.    
                1 -> 2 -> 3 -> 4 -> 5
        '''
        pass 



