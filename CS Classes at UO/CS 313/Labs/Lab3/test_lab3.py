import lab3
import unittest


class T0_tree__insert(unittest.TestCase):
    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()
        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        # The following check is without using tree as an iterator (which uses inorder traversal)
        # So this function also does not check the implementation of the traversal function
        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)
        print("\n")


class T1_min_and_max(unittest.TestCase):
    def test_min_and_max(self):
        print("\n")
        print("Checking the min and the max functions")
        t = lab3.Tree()
        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        minimum = t.min()
        self.assertEqual(minimum, 1)
        maximum = t.max()
        self.assertEqual(maximum, 7)
        print("\n")


class T2_Traversal(unittest.TestCase):
    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()
        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("\n")

    def test_traversal_2(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()
        t.insert(104)
        t.insert(102)
        t.insert(106)
        t.insert(101)
        t.insert(103)
        t.insert(105)
        t.insert(107)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [101, 102, 103, 104, 105, 106, 107])
        print("inorder traversal")
        self.assertEqual(inorder, [101, 102, 103, 104, 105, 106, 107])
        print("preorder traversal")
        self.assertEqual(preorder, [104, 102, 101, 103, 106, 105, 107])
        print("\n")


class T3_successor(unittest.TestCase):
    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)
        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data
        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)
        print("\n")

    def test_successor_2(self):
        tree_success = lab3.Tree()
        tree_success.insert(108)
        tree_success.insert(103)
        tree_success.insert(110)
        tree_success.insert(101)
        tree_success.insert(106)
        tree_success.insert(104)
        tree_success.insert(107)
        tree_success.insert(114)
        tree_success.insert(113)
        easy_success = tree_success.find_successor(108).data
        medium_success = tree_success.find_successor(110).data
        tough_success = tree_success.find_successor(107).data
        self.assertEqual(easy_success, 110)
        self.assertEqual(medium_success, 113)
        self.assertEqual(tough_success, 108)
        print("\n")

    def test_successor_error(self):
        tree_success = lab3.Tree()
        tree_success.insert(8)
        with self.assertRaises(KeyError):
            tree_success.find_successor(8).data


class T4_delete(unittest.TestCase):
    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]
        self.assertEqual(l1, [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10, 13, 14])
        self.assertEqual(l3, [1, 3, 4, 8, 10, 13, 14])
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])
        print("\n")

    def test_delete_2(self):
        t = lab3.Tree()
        t.insert(108)
        t.insert(103)
        t.insert(110)
        t.insert(101)
        t.insert(106)
        t.insert(104)
        t.insert(107)
        t.insert(114)
        t.insert(113)
        l1 = [node for node in t]
        t.delete(107)
        l2 = [node for node in t]
        t.delete(106)
        l3 = [node for node in t]
        t.delete(108)
        l4 = [node for node in t]
        t.delete(110)
        l5 = [node for node in t]
        self.assertEqual(l1, [101, 103, 104, 106, 107, 108, 110, 113, 114])
        self.assertEqual(l2, [101, 103, 104, 106, 108, 110, 113, 114])
        self.assertEqual(l3, [101, 103, 104, 108, 110, 113, 114])
        self.assertEqual(l4, [101, 103, 104, 110, 113, 114])
        self.assertEqual(l5, [101, 103, 104, 113, 114])
        print("\n")

    def test_delete_error(self):
        t = lab3.Tree()
        t.insert(8)
        t.delete(8)
        with self.assertRaises(KeyError):
            t.delete(8)


class T5_contains(unittest.TestCase):
    def test_contains(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")

    def test_contains_2(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        t.insert(108)
        t.insert(103)
        t.insert(110)
        t.insert(101)
        t.insert(106)
        t.insert(104)
        t.insert(107)
        t.insert(114)
        t.insert(113)
        self.assertEqual(t.contains(113), True)
        self.assertEqual(t.contains(115), False)
        print("\n")


if __name__ == '__main__':
    unittest.main()