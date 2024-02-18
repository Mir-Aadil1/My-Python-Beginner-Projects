class SLLNode:

    def __init__(self, data):
        self.data = data 
        self.next = None 



    def get_data(self):
        """Return the self.data attribute"""
        return self.data 
    
    def __repr__(self):
        return "SLLNode Object: data={}".format(self.data)

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data parameters"""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next parameters"""
        self.next = new_next


#  Linked lists don't contain nodes, instead they have a head attribute that points to first node of the linked list if one exists , otherwise to None 
        



class SLL:
    def __init__(self):
        self.head = None 

    def __repr__(self):
        return "SLL object: head={}".format(self.head)
    

    def is_empty(self):
        """Returns True if the Linked List is empty otherwise,returns False"""
        return self.head is None  # self.head == None 

    def add_front(self, new_data):
        """Add a Node whose data is the new_data argument to the front of the list"""
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp 

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

    def remove(self, data):
        """Removes the first occurence of a Node that contains the data argument as its self.data variable. Returns nothing
         The time complexity is o(n) because in the worst case we have to visit every Node before we find the one to Remove
         """
        # Edge Case 1 : Empty Linked List 
        # Edge Case 2 : Target Data Not Found
        # Case 3 : if the Node to Remove is the First Node  (self.head = current.get_next())
        # Case 4 : Removing Nodes Elsewhere (previous.set_next(current.get_next))

        if self.head is None:
            return "The linked list is empty , No Nodes to remove"
        current = self.head 
        previous = None 
        found = False 
        while not found:
            if current.get_data() == data:
                found = True 
            else:
                if current.get_next() == None:
                    return "A Node with that data value is not present"
                else:
                    previous = current
                    current = current.get_next()
        if previous is None:
            self.head = current.get_next()

        else:
            previous.set_next(current.get_next())


