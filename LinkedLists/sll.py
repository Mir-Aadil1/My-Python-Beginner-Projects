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
        pass 

    def size(self):
        pass 

    def search(self, data):
        pass 

    def remove(self, data):
        pass 



