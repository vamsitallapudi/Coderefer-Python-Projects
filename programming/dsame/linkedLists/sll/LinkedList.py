class Node:
    def __init__(self, data):
        self.data = data  # assigning the data passed
        self.next = None  # initializing the node as null


class LinkedList:
    def __init__(self):
        self.head = None


# actual code execution starts from here
if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.head = Node('a')  # pointed linkedlist's head to node 'a'
    second = Node('b')  # created a simple new second node
    third = Node('c')   # created a simple new third node

    ''' 
    We created 3 nodes as follows:

    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  | None |     | 2  | None |     |  3 | None | 
    +----+------+     +----+------+     +----+------+ 
    '''

#     now linking second node to linked list's head node
    linkedList.head.next = second

    ''' 
     Now next of first Node refers to second.  So they 
     both are linked. 

     llist.head        second              third 
          |                |                  | 
          |                |                  | 
     +----+------+     +----+------+     +----+------+ 
     | 1  |  o-------->| 2  | null |     |  3 | null | 
     +----+------+     +----+------+     +----+------+  
     '''

    # linking third node to second node
    second.next = third

    ''' 
    Now next of second Node refers to third.  So all three 
    nodes are linked. 

    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''

