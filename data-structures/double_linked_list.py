"""
A simpel module for Doubly linked list representation
"""

class Node:
    """
    A class to create node for double linked list
    """
    def __init__(self, value):
        """
        Initializing the next and prev pointer with None for each node when created
        """
        self.next = None
        self.prev = None
        self.val = value


class DoubleLinkedList:
    """
    A class for creating the double linked list
    """
    def __init__(self):
        """
        Initializing the head and tail as None when instantiating the double linked list
        """
        self.head = None
        self.tail = None
        self.size = 0


    def add(self, value):
        """
        A method for adding new node to the double linked list
        """
        node = Node(value)

        # if the double linked list is empty then creating the first node in the list is a exceptional case
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        # if the double linked list is not empty, then it is a general case for all the node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1


    def remove(self, value):
        """
        A method for removing node from the double linked list by value
        """
        node = self.head

        while node is not None:
            if node.val == value:
                if node.prev is None:
                    self.head = node.next
                else:
                    node.prev.next = node.next
                
                if node.next is None:
                    self.tail = node.prev
                else:
                    node.next.prev = node.prev

                # we can use break, if we want to only remove the first occurrence
                # break
                # if we wanto to remove all the occurrences, then no need to break until reaching the end of the list

            node = node.next

    def get_list_content(self):
        """
        A simple method that returns all the items from the double linked list
        """
        vals = []
        node = self.head

        while node is not None:
            vals.append(node.val)
            node = node.next
        
        return vals



if __name__ == '__main__':
    my_list = DoubleLinkedList()
    my_list.add(1)
    my_list.add(5)
    my_list.add(2)
    my_list.add(7)

    print(my_list.get_list_content())

    my_list.remove(1)
    print(my_list.get_list_content())