class Node(object):
    """
    A class to represent a node.
    ...
    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue
    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """
    def __init__(self, data = None, next_node = None):
        """
        Constructs (or initializes) the attributes for an object of the class
        ...
        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue
        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        """
        Set the "data" data field to the corresponding input.

        ...
        Parameters
        ----------
        data: int or float
            a character or number that is stored in a node
        """
        self.__data = data

    def setNext(self, next_node):
        """
        Set the "next_node" data field to the corresponding input.

        ...
        Parameter
        ---------
        next_node: object of class Node
            pointer for next node in stack or queue
        """
        self.__next_node = next_node

    def getData(self):
        """Return the "data" data field."""
        return self.__data

    def getNext(self):
        """Return the "next_node" data field."""
        return self.__next_node

class Queue(object):
    """
    A class to represent a queue
    ...
    Attributes
    ----------
    self.__head: int or float
        first value of queue list
    self.__tail: int or float
        last value of queue list
    newData(): int or float
        character or number stored in a node
    Methods
    -------
    enqueue(newData):
        takes a temporary node and stores it to queue
    dequeue():
        returns head of queue in (order is first in last out)
    isEmpty():
        checks to see if head is empty
    """
    def __init__(self):
        "initialize head and tail to be empty"
        self.__head = None
        self.__tail = None

    def __str__(self):
        """Loop through your queue and print each Node's data."""
        if self.__head is None:
            return None
        node = self.__head
        result = "["
        while node is not None:
            result += str(node.getData()) + ", "
            node = node.getNext()
        return result[:-2] + "]"

    def enqueue(self, newData):
        """
        Create a new node whose data is newData and whose next node is null
        Update head and tail.

        ...
        Parameter
        ---------
        newData: int or float
            a new number or character that will be stored in a node
        """
        # Hint: Think about what's different for the first node added to the Queue
        if self.__head is None:
            self.__head = self.__tail = Node(newData)
        else:
            node = Node(newData)
            self.__tail.setNext(node)
            self.__tail = node

    def dequeue(self):
        """Return the head of the Queue
        Update head."""
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #  to hold important information
        #  Hint: Return null on a empty Queue
        #  Hint: Return the element(data) that is dequeued.
        try:
            node = self.__head
            if self.__tail == self.__head:
                self.__tail = self.__head = None
            else:
                self.__head = node.getNext()
            return node.getData()
            raise AttributeError

        except AttributeError:
            print("[]")
            raise AttributeError

    def isEmpty(self):
        """Check if the Queue is empty."""
        return self.__head is None

class Stack(object):
    """
    A class to represent a stack

    ...
    Attributes
    ----------
    self.stack: int or float
        top of the stack

    newData(): int or float
        character or number stored in a node
    Methods
    -------
    push(newData):
        creates a temporary node to put the data on the top of the stack
    pop():
        returns head of queue in (order is first in last out)
    isEmpty():
        checks to see if stack is empty
    """
    def __init__(self):
        """We want to initialize our Stack to be empty.
        (ie) Set top as null"""
        self.stack = None

    def __str__(self):
        """Loop through your stack and print each Node's data."""
        if self.stack is None:
            return None
        node = self.stack
        result = "["
        while node is not None:
            result += str(node.getData()) + ", "
            node = node.getNext()
        return result[:-2] + "]"

    def push(self, newData):
        """
        We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top

        ...
        Parameter
        ---------
        newData: int or float
            a new number or character that will be stored in a node
        """
        node = Node(newData, self.stack)
        self.stack = node

    def pop(self):
        """Return the Node that currently represents the top of the stack.
        Update top"""
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        # to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        try:
            node = self.stack
            self.stack = node.getNext()
            return node.getData()
        except AttributeError:
            print("[]")

    def isEmpty(self):
        """Check if the Stack is empty."""
        return self.stack is None

def isPalindrome(s):
    """
    Use your Queue and Stack class to test whether an input is a palindrome.

    ...
    Parameter
    ---------
    s: string
        tests the string to see if it is a palindrome
    """
    myStack = Stack()
    myQueue = Queue()
    # Helper function:
    # print("stack data")
    # myStack.printStack()
    # print("queue data")
    # myQueue.printQueue()
    # Return appropriate value
    for c in s.replace(" ","").lower():
        myStack.push(c)
        myQueue.enqueue(c)
    print(myQueue)
    print(myStack)
    while not myStack.isEmpty():
        if myStack.pop() is not myQueue.dequeue():
            return False
    return True
