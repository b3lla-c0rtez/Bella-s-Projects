class max_heap(object):
    """
    Worked together on this assignment with Sequoia, Willard, Lynette, and Sam

    Binary max-heap
    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.

    Methods
    _______
    get_heap
        returns heap

    insert(data)
        Insert an element into the heap.
        Raises IndexError if the heap is full.

    peek
        Return the maximum value in the heap.

    extract_max
        Remove and return the maximum value in the heap.
        Raises KeyError if the heap is empty.

    __heapify(curr_index, list_length=None)
        heapify moves elements down in a heap

    build_heap
        builds max heap from the list l

    __get_parent(loc)
        gets the root or parent of the list

    __get_left(loc)
        gets the left child of the list

    __get_right(loc)
        gets the right child of the list

    swap(a, b)
        swap elements located at indexes
        a and b of the heap
    """

    def __init__(self, size=20, data=None):
        """
        Initialize a binary max-heap.

        ...
        Parameters
        __________
        size: int
            Total capacity of the heap.
        data: list
            List containing the desired heap contents.
            The list is used in-place, not copied, so its contents
            will be modified by heap operations.
            If data is specified, then the size field is ignored.
        """
        # Add to this constructor as needed
        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size

    def get_heap(self):
        """returns get heap"""
        return self.heap

    def insert(self, data):
        """
        Insert an element into the heap.
        Raises IndexError if the heap is full.

        ...
        Parameter
        _________
        data: int
            takes the int and inserts it into the heap list
            data gets swapped until it reaches the root

        Raises
        ______
        IndexError
            if the length of the list is greater than the size that
            it can be when something is inserted
        """
        # Tips : insert 'data' at the end of the list initially
        #      : swap with its parent until the parent is larger or you
        #      : reach the root

        if self.length >= self.max_size:
            raise IndexError
        if self.length == 0:
            self.heap[0] = data
            self.length += 1
        else:
            self.heap[self.length] = data
            self.length += 1
        current = self.length-1
        while self.heap[current] and self.heap[self.__get_parent(current)] and (current != 0) and (self.heap[current] > self.heap[self.__get_parent(current)]):
            self.__swap(current, self.__get_parent(current))
            current = self.__get_parent(current)

    def peek(self):
        """
        Return the maximum value in the heap.

        Returns
        _______
            returns "heap is empty" if length of heap is 0
            returns the value of the heap at index 0 if heap is not empty
        """
        if len(self.heap) != 0:
            return (self.heap[0])
        else:
            return "heap is empty"

    def extract_max(self):
        """
        Remove and return the maximum value in the heap.
        Raises KeyError if the heap is empty.

        Returns
        _______
            None of self.length is less than or
            equal to 0 or if it is none

            Popped if self.length is not none or is greater than 0

        Raises
        ______
        Key Error
            if there are no elements in the list and
            something is extracted
        """
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap
        if self.length == None or self.length<=0:
            raise KeyError
            return None

        popped = self.heap[0]
        self.heap[0] = self.heap[self.length-1]
        self.heap[self.length-1] = None
        self.length -= 1
        self.__heapify(0, self.length)

        return popped

    def __heapify(self, curr_index, list_length=None):
        """
        heapify moves elements down in a heap

        ...
        Parameters
        ----------
        curr_index: int
            the current index or current value of a list
        list_length: None
            list length is an int
            length of the list
        """
        # helper function for moving elements down in the heap
        # Page 157 of CLRS book
        l = self.__get_left(curr_index)
        r = self.__get_right(curr_index)
        if l <= list_length-1 and self.heap[l] > self.heap[curr_index]:
            largest = l
        else:
            largest = curr_index
        if r <= list_length-1 and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != curr_index:
            self.heap[curr_index], self.heap[largest] = self.heap[largest], self.heap[curr_index]
            self.__heapify(largest, list_length)

    def build_heap(self):
        """builds max heap from the list l"""
        # Tip: call __heapify() to build to the list
        #    : Page 157 of CLRS book
        for i in range((self.length//2), -1,  -1):
            self.__heapify(i, self.length)


    def __get_parent(self, loc):
        """
        gets the root or parent of the list

        ...
        Parameter
        _________
        loc: int
            the location index of a node

        Returns
        _______
            the parent of a node
        """
        # left child has odd location index
        # right child has even location index
        if loc % 2 == 0:
            parent = int((loc - 2) / 2)
        else:
            parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        """
        gets the left child of the list

        ...
        Parameter
        _________
        loc: int
            the location index of a node

        Returns
        _______
            the left child of a node
        """
        return 2 * loc + 1

    def __get_right(self, loc):
        """
        gets the right child of the list

        ...
        Parameter
        _________
        loc: int
            the location index of a node

        Returns
        _______
            returns the right child of a node
        """
        return 2 * loc + 2

    def __swap(self, a, b):
        """
        swap elements located at indexes a and b of the heap

        ...
        Parameters
        __________
        a: int
            element located at index a
        b: int
            element located at index b
        """
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp


def heap_sort(l):
    """
    Sort a list in place using heapsort.

    ...
    Parameter
    _________
    l: list
        the list that gets sorted
    """
    # Note: the heap sort function is outside the class
    #     : The sorted list should be in ascending order
    # Tips: Initialize a heap using the provided list
    #     : Use build_heap() to turn the list into a valid heap
    #     : Repeatedly extract the maximum and place it at the end of the list
    #     : Refer page 161 in the CLRS textbook for the exact procedure
    n = len(l)
    heap = max_heap(n,l)
    listL = [None] * n

    heap.build_heap()

    while heap.length > 0:
        index = heap.extract_max()
        listL[heap.length] = index
    return listL




