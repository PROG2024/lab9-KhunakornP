"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class CounterTest(unittest.TestCase):
    def test_counter_is_singleton(self):
        """Counter should have the same id"""
        original_id = id(Counter())
        counter2 = Counter()
        self.assertEqual(original_id, id(counter2))
        self.assertTrue(Counter() == counter2)

    def test_counter_remembers_count(self):
        """Counter should be able to increment and keep its count"""
        counter = Counter()
        self.assertEqual(0, counter.count)
        counter.increment()
        self.assertEqual(1, counter.count)
        counter.increment()
        self.assertEqual(2, counter.count)
        counter2 = Counter()
        self.assertEqual(2, counter2.count)
