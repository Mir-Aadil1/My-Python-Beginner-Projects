class DLLNODE:

    def __init__(self, data):
        self.data = data 
        self.next = None
        self.previous = None



    def get_data(self):
        """Return the self.data attribute"""
        return self.data 
    
    def __repr__(self):
        return "DLLNode Object: data={}".format(self.data)

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data parameters"""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next
    
    def get_previous(self):
        """Return the self.previous attribute"""
        return self.previous

    def set_previous(self, new_previous):
        """Replace the existing value of the self.previous attribute with new_previous parameter"""
        self.previous = new_previous

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next parameters"""
        self.next = new_next


class DLL:
    def __init__(self):
        self.head = None 

    def __repr__(self):
        return "<DLL Object: head={}>".format(self.head)
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        """ Traversse the Linked List and returns an integer value representing the number of nodes in the Linked List
        
        The time complexity is O(n) because every Node in the Linked List must be visited in order to calculate the size of the Linked List.
        """
        size = 0
        if self.head is None:
            return size 

        current = self.head 

        while current is not None: # while there are still Nodes left to count 
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """ Traverses teh Linked List and return True if the data searched for is present in one of the Nodes. Otherwise, it returns Fasle 
        
        The time complexity is O(n) becuase in the worst case we have to go through every node to either find or not find it .
        
        """
        if self.head is None:
            return "Linked List is empty , No Nodes to search."

        current = self.head 

        while current is not None:
            # The Node's data matches what we're looking for
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
            # The Node's  data doesn't match

        return False 

    def add_front(self, new_data):
        """Add a Node whose data is the new_data argument to the front of the list"""
        temp = DLLNODE(new_data)
        temp.set_next(self.head)
        if self.head is not None:
            self.head.set_previous(temp)
        self.head = temp 

    def remove(self, data):
        pass 