# Data Structures & Algorithms
# Tutorial 6: Linked Lists
# Name: TODO Write your name here
# NPM: TODO Write your NPM here

"""
Implement a linked list by completing all the methods for ListNode
and LinkedList. Make sure to put in comments, remove the 'pass'
statement in each method after implementing it, and verify that
the main() method outputs the output provided in the comments on
each line.
"""

class ListNode:

    def __init__(self, data=None, next=None):
        """ The node provides the data and a pointer 
            to the next node. """
        pass
        
    def __repr__(self):
        """ Returns a string in the format of ListNode(x)
            where x is the node's data value. """
        return "ListNode({})".format(self.data)
    
class LinkedList:
    
    def __init__(self, head=None):
        """ The linked list provides the first node
            (self.head) of the linked list. """
        self.head = head
        
    def size(self):
        """ Returns the count of the nodes in the
            linked list. """ 
        pass
    
    def search(self, data):
        """ Searches the list for a node holding a
            given data value. Returns the node object
            if found, else prints "Data not found.",
            then returns None. If the list is empty,
            returns None. """
        if self.head is None:
            pass
        current = self.head
        found = False
        while not found and current:
            pass
        if not found:
            print("Data not found.")
        return current
            
    def insert(self, data):
        """ Inserts a new node with the given data
            value on the beginning of the list.
            Does not allow duplicates. Returns
            True upon completion. If a duplicate
            exists, prints "Cannot add duplicate."
            and returns None. """
        pass
        
    def delete(self, data):
        """ Deletes a node holding a given data value.
            If the node to be deleted is not found,
            prints "Data not found." and returns None.
            Else, returns True. If the list is empty,
            returns None. """
        pass
            
    def print_list(self):
        """ Prints the nodes in the list one by one.
            HINT: Use the given ListNode.__repr__()
                  function and print the ListNode
                  item with the node as the parameter
                  without accessing ListNode.data. """
        pass
            
if __name__ == "__main__":
    my_list = LinkedList(ListNode(5, ListNode(7, ListNode(11))))
    my_list.insert(3)       
    my_list.insert(5)           # Cannot add duplicate.
    print(my_list.search(11))   # ListNode(11)
    print(my_list.size())       # 4
    my_list.print_list()        # ListNode(3), ListNode(5), 
                                # ListNode(7), ListNode(11)
    my_list.delete(11)      
    my_list.delete(1)           # Data not found.
    my_list.search(11)          # Data not found.
    my_list.print_list()        # ListNode(3), ListNode(5), ListNode(7)