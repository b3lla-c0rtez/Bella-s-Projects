import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):
    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5, 4, 2, 1, 3])
        print("\n")

    def test_2_pq_is_int(self):
        print("\n")
        pq = pqueue.pqueue(8)
        pq.insert(4)
        pq.insert(6)
        pq.insert(8)
        self.assertEqual(isinstance(pq.peek(), int), True)
        print("\n")

    def test_3_pq_peek_in_empty(self):
        print("\n")
        pq = pqueue.pqueue(4)
        pq.insert(5)
        pq.insert(6)
        pq.insert(7)
        pq.insert(8)
        for i in pq:
            pq.extract_max()
        self.assertEqual(pq.peek(), None)
        print("\n")

class T1_pqueue_peek(unittest.TestCase):
    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")


class T2_pqueue_extract_max(unittest.TestCase):
    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")

    def test_2_pq_extract_max(self):
        print("\n")
        pq = pqueue.pqueue(10)
        with self.assertRaises(KeyError):
            pq.extract_max()
        print("\n")

    def test_3_pq_extract_max(self):
        print("\n")
        pq = pqueue.pqueue(10)
        pq.insert(4)
        self.assertEqual(pq.extract_max(), 4)
        print("\n")

    def test_4_pq_size(self):
        print("\n")
        pq = pqueue.pqueue(3)
        pq.insert(2)
        pq.insert(4)
        pq.insert(5)
        with self.assertRaises(IndexError):
            pq.insert(6)
        print("\n")

    def test_5_pq_extract_max(self):
        print("\n")
        pq = pqueue.pqueue(6)
        pq.insert(2)
        self.assertEqual(pq.extract_max(), 2)
        pq.insert(4)
        pq.insert(10)
        self.assertEqual(pq.extract_max(), 10)
        pq.insert(12)
        pq.insert(20)
        self.assertEqual(pq.extract_max(), 20)
        print("\n")

    def test_6_pq_extract_max_empty(self):
        print("\n")
        pq = pqueue.pqueue(10)
        with self.assertRaises(KeyError):
            pq.extract_max()
        print("\n")

    def test_7_pq_empty(self):
        print("\n")
        pq = pqueue.pqueue(11)
        self.assertEqual(pq.is_empty(), True)
        print("\n")

    def test_8_pq_empty_after_insert(self):
        print("\n")
        pq = pqueue.pqueue(11)
        pq.insert(6)
        self.assertEqual(pq.is_empty(), False)
        print("\n")

class T3_test_build_heap(unittest.TestCase):
    def test_build_heap(self):
        print("\n")
        l_to_h = [1, 2, 3, 4]
        mhp = mheap.max_heap(len(l_to_h), l_to_h)
        mhp.build_heap()
        self.assertEqual(mhp.get_heap(), [4, 2, 3, 1])
        print("\n")

if __name__ == '__main__':
    unittest.main()