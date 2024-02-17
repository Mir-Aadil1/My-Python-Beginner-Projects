class SLLNODE:

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
