class Node(object):
    """
    Node class that has parent of node, left child and right child, and data

    ...
    Parameters
    ----------
    data: int
        the data value of a node in a tree
    """
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    """
    Tree class with methods that help build a binary search tree

    ...
    Methods:
    --------
    print
        prints data of all nodes in order
    __print(curr_node)
        recursively prints a subtree
    insert(data)
        finds the spot in the tree for a node
    min
        returns min value in a tree
    max
        returns max value in a tree
    __find_node(data)
        returns the node with that particular data
    contains(data)
        return True of node containing data is present in the tree, otherwise false
    __iter__
        iterate over the nodes with inorder traversal using a for loop
    inorder
        inorder traversal
    preorder
        preorder traversal
    postorder
        postorder traversal
    __traverse(curr_node, traversal_type)
        all the traversals can be implemented using a single method
    find_successor(data)
        finds the successor node
    delete(data)
        finds the node to delete
    """
    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        """
        Print the data of all nodes in order
        """
        self.__print(self.root)

    def __print(self, curr_node):
        """
        Recursively print a subtree (in order), rooted at curr_node
        """
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)

    def insert(self, data):
        """
        Finds the right spot in the tree for the new node

        Parameter
        ---------
        data: int
            the node value
        """
        r = self.root
        n = Node(data)
        y = None
        while r is not None:
            y = r
            if n.data < r.data:
                r = r.left
            else:
                r = r.right
        n.parent = y
        if y is None:
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n


    def min(self):
        """
        Returns the minimum value held in the tree
        Returns None if the tree is empty
        """
        r = self.root
        while r.left is not None:
            r = r.left
        return r.data


    def max(self):
        """
        Returns the maximum value held in the tree
        Returns None if the tree is empty
        """
        r = self.root
        while r.right is not None:
            r = r.right
        return r.data

    def __find_node(self, data):
        """
        returns the node with that particular data value else returns None

        Parameter
        ---------
        data: int
            the node value
        """
        r = self.root
        while r is not None and data is not r.data:
            if data < r.data:
                r = r.left
            else:
                r = r.right
        return r

    def contains(self, data):
        """
        return True of node containing data is present in the tree.
        otherwise, return False.

        Parameter
        ---------
        data: int
            the node value
        """
        n = self.__find_node(data)
        if n is None:
            return False
        else:
            return True


    def __iter__(self):
        """
        iterate over the nodes with inorder traversal using a for loop
        """
        return self.inorder()


    def inorder(self):
        """
        inorder traversal : (LEFT, ROOT, RIGHT)
        """
        return self.__traverse(self.root, Tree.INORDER)


    def preorder(self):
        """
        preorder traversal : (ROOT, LEFT, RIGHT)
        """
        return self.__traverse(self.root, Tree.PREORDER)


    def postorder(self):
        """
        postorder traversal : (LEFT, RIGHT, ROOT)
        """
        return self.__traverse(self.root, Tree.POSTORDER)


    def __traverse(self, curr_node, traversal_type):
        """
        all the traversals can be implemented using a single method

        Parameter
        ---------
        curr_node: self.root
            if it is self.root.right, self.root.left, or self.root
        traversal_type: the traverse method type
            if it is inorder, preorder, or postorder
        """
        if curr_node is not None:
            if traversal_type is self.INORDER:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield (curr_node.data)
                yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type is self.PREORDER:
                yield (curr_node.data)
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type is self.POSTORDER:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
                yield (curr_node.data)
        else:
            return None


    def find_successor(self, data):
        """
        finds the successor node
        Return object of successor if found else return None

        Parameter
        ---------
        data: int
            the node value

        Raises
        ------
        KeyError
            If the value specified by find_successor does NOT exist in the tree
        """
        r = self.root
        n = self.__find_node(data)
        if self.root is None:
            raise KeyError
        if n is None:
            raise KeyError
        if n.right is not None:
            n = n.right
            while n.left is not None:
                n = n.left
            ancestor = n
            return ancestor
        else:
            y = n.parent
            x = n
            while y is not None and x is y.right:
                x = y
                y = x.parent
            return y


    def delete(self, data):
        """Find the node to delete.

        Parameter
        ---------
        data: int
            the node value

        Raises
        ------
        KeyError
            If the value specified by delete does NOT exist in the tree, then don't change the tree
        """
        r = self.root
        n = self.__find_node(data)
        p = None

        if self.root is None:
            raise KeyError

        if not self.contains(data):
            raise KeyError

        if self.root.data == data and self.root.left is None and self.root.right is None:
            self.root = None

        while (r is not None and r.data is not n.data):
            p = r
            if r.data < n.data:
                r = r.right
            else:
                r = r.left
        if r is None:
            return r
        if r.left is None or r.right is None:
            newR = None
            if r.left is None:
                newR = r.right
            else:
                newR = r.left
            if p is None:
                return newR
            if r is p.left:
                p.left = newR
            else:
                p.right = newR
            r = None
        else:
            x = None
            y = None
            y = r.right
            while y.left is not None:
                x = y
                y = y.left
            if x is not None:
                x.left = y.right
            else:
                r.right = y.right
            r.data = y.data
            y = None
        return r