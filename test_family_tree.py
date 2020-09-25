from unittest import TestCase
from family_tree import Node


class TestNode(TestCase):

    def test_create_family_tree(self):
        # Base case
        root = Node.create_family_tree(input_string="None,0,grandpa|0,1,son|0,2,daugther|1,3,grandkid|1,4,"
                                                    "grandkid|2,5,grandkid|5,6,greatgrandkid")

        testlist = root.display_tree(test_list=[])
        expected_list = [{'grandpa': 0}, {'son': 1}, {'grandkid': 2}, {'grandkid': 2},
                         {'daugther': 1}, {'grandkid': 2}, {'greatgrandkid': 3}]
        self.assertListEqual(testlist, expected_list)

    def test_create_family_tree_empty(self):
        # Empty string - border case
        root = Node.create_family_tree(input_string="")

        self.assertIsNone(root)

    def test_create_family_tree_only_grandpa(self):
        # Just one node - border case
        root = Node.create_family_tree(input_string="None,0,grandpa|")
        testlist = root.display_tree(test_list=[])
        expected_list = [{'grandpa': 0}]
        self.assertListEqual(testlist, expected_list)

    def test_create_skip_generation(self):
        # Not all in a generation have children
        root = Node.create_family_tree(input_string="None,0,Smith|0,1,Conor|0,2,Cooper|1,3,Alexis|1,4,Sue|2,5,Max|2,6,"
                                                    "Elvis|2,7,Steven|3,8,Joe|5,9,Luis|8,10,Clark")

        testlist = root.display_tree(test_list=[])
        print(testlist)
        expected_list = [{'Smith': 0}, {'Conor': 1}, {'Alexis': 2}, {'Joe': 3}, {'Clark': 4}, {'Sue': 2}, {'Cooper': 1},
                         {'Max': 2}, {'Luis': 3}, {'Elvis': 2}, {'Steven': 2}]
        self.assertListEqual(testlist, expected_list)
