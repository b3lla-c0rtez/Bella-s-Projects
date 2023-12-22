import lab1
import unittest

class T0_TestingQueue(unittest.TestCase):
    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')
        print("\n")
        print(q)

class T1_TestingStack(unittest.TestCase):
    def test_is_empty_false(self):
        # testing if stack is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")
        print(s)

class T2_TestingStack(unittest.TestCase):
    def test_basic_push(self):
        # testing the basic stack operation
        print("\n")
        a = lab1.Stack()
        a.push(1)
        a.push(2)
        a.push(3)
        a.push(4)
        self.assertEqual(a.__str__(), '[4, 3, 2, 1]')
        print("\n")
        print(a)


class T3_TestingPalindrome(unittest.TestCase):
    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)
        print("\n")
        print(p)

class T4_TestingPalindrome(unittest.TestCase):
    def test_basic_string2(self):
        # testing with basic string
        print("\n")
        string2 = "TaCo Cat"
        p2 = lab1.isPalindrome(string2)
        print("The string being tested is -> ", string2)
        self.assertEqual(p2, True)
        print("\n")
        print(p2)

class T5_TestingPalindrome(unittest.TestCase):
    def test_basic_string3(self):
        # testing with basic string
        print("\n")
        string3 = "12TENET12"
        p3 = lab1.isPalindrome(string3)
        print("The string being tested is -> ", string3)
        self.assertEqual(p3, False)
        print("\n")
        print(p3)

class T6_TestingPalindrome(unittest.TestCase):
    def test_basic_string4(self):
        # testing with basic string
        print("\n")
        string4 = "ni t I n"
        p4 = lab1.isPalindrome(string4)
        print("The string being tested is -> ", string4)
        self.assertEqual(p4, True)
        print("\n")
        print(p4)

class T7_TestingPalindrome(unittest.TestCase):
    def test_basic_string5(self):
        # testing with basic string
        print("\n")
        string5 = "&$(^^)$&"
        p5 = lab1.isPalindrome(string5)
        print("The string being tested is -> ", string5)
        self.assertEqual(p5, False)
        print("\n")
        print(p5)

class T8_TestingPalindrome(unittest.TestCase):
    def test_basic_string6(self):
        # testing with basic string
        print("\n")
        string6 = "My gym"
        p6 = lab1.isPalindrome(string6)
        print("The string being tested is -> ", string6)
        self.assertEqual(p6, True)
        print("\n")
        print(p6)

class T9_TestingPalindrome(unittest.TestCase):
    def test_basic_string6(self):
        # testing with basic string
        print("\n")
        string7 = "63488436"
        p7 = lab1.isPalindrome(string7)
        print("The string being tested is -> ", string7)
        self.assertEqual(p7, True)
        print("\n")
        print(p7)

class T10_TestingStack(unittest.TestCase):
    def test_is_empty_false2(self):
        # testing if stack is empty
        print("\n")
        e = lab1.Stack()
        e.push("3")
        e.push("4")
        e.pop()
        print("return false if the stack is not empty")
        self.assertEqual(e.isEmpty(), False)
        print("\n")
        print(e)

class T11_TestingQueue(unittest.TestCase):
    def test_basic_enqueue2(self):
        # testing the basic enqueue operation
        print("\n")
        u = lab1.Queue()
        u.enqueue(1)
        u.enqueue(2)
        u.dequeue()
        print("return false if the queue is not empty")
        self.assertEqual(u.isEmpty(), False)
        print("\n")
        print(u)

class T12_TestingQueue(unittest.TestCase):
    def test_basic_enqueue3(self):
        # testing the basic enqueue operation
        print("\n")
        f = lab1.Queue()
        f.enqueue(1)
        f.dequeue()
        print("return false if the queue is not empty")
        self.assertEqual(f.isEmpty(), True)
        print("\n")

class T13_TestingStack(unittest.TestCase):
    def test_is_empty_true(self):
        # testing if stack is empty
        print("\n")
        b = lab1.Stack()
        b.push(3)
        b.pop()
        print("return false if the stack is not empty")
        self.assertEqual(b.isEmpty(), True)
        print("\n")

class T14_TestingStack(unittest.TestCase):
    def test_is_empty_false2(self):
        # testing if stack is empty
        print("\n")
        c = lab1.Stack()
        c.push("")
        print("return false if the stack is not empty")
        self.assertEqual(c.isEmpty(), False)
        print("\n")
        print(c)

class T15_TestingQueue(unittest.TestCase):
    def test_basic_enqueue2(self):
        # testing the basic enqueue operation
        print("\n")
        d = lab1.Queue()
        d.enqueue("")
        print("return false if the queue is not empty")
        self.assertEqual(d.isEmpty(), False)
        print("\n")
        print(d)

if __name__ == '__main__':
    unittest.main()