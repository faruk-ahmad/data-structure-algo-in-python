"""
A test module to test the double linked list class
"""

# lets import the unittest module
import unittest
import sys

# since the double_linked_list module is upper level module from the test module, lets append the path
sys.path.append('..')
from double_linked_list import DoubleLinkedList 

class TestDoubleLinkedList(unittest.TestCase):
    """
    A test class for testing the DoubleLinkedList class
    """

    def setUp(self):
        """
        A setup method for instantiating the DoubleLinkedList class for using throughout the whole test class
        """
        self.dbl_list = DoubleLinkedList()

    def test_add_1(self):
        """
        Test for adding single element in the double linked list
        """
        self.dbl_list.add(5)
        contents = self.dbl_list.get_list_content()
        self.assertEqual(contents , [5], "Can not add element 5")

    def test_add_2(self):
        """
        Test for adding multiple elements in the double linked list
        """
        self.dbl_list.add(5)
        self.dbl_list.add(2)
        contents = self.dbl_list.get_list_content()
        self.assertEqual(contents, [5, 2], "Can not add two elements")


    def test_remove_first(self):
        """
        Test for removing the first element from the double linked list
        """
        self.dbl_list.add(5)
        self.dbl_list.add(7)
        self.dbl_list.remove(5)

        contents = self.dbl_list.get_list_content()
        self.assertEqual(contents, [7], "Can not delete the first element")


    def test_remove_last(self):
        """
        Test for removing the last element from the double linked list
        """
        self.dbl_list.add(5)
        self.dbl_list.add(2)
        self.dbl_list.remove(2)

        contents = self.dbl_list.get_list_content()
        self.assertEqual(contents, [5], "Can not remove last element")

    def test_remove_middle(self):
        """
        Test for removing the middle element from the double linked list
        """
        self.dbl_list.add(4)
        self.dbl_list.add(5)
        self.dbl_list.add(2)
        self.dbl_list.remove(5)

        contents = self.dbl_list.get_list_content()
        self.assertEqual(contents, [4, 2], "Can not remove middle element")