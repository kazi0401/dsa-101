import unittest

class TestMyHashMap(unittest.TestCase):

    def setUp(self):
        from myhashmap import MyHashMap  # Assuming your class is in my_hash_map.py
        self.map = MyHashMap(10)

    def test_put_and_get_single_item(self):
        self.map.put("apple", 5)
        self.assertEqual(self.map.get("apple"), 5)

    def test_put_overwrites_existing_key(self):
        self.map.put("apple", 5)
        self.map.put("apple", 10)
        self.assertEqual(self.map.get("apple"), 10)

    def test_get_missing_key_returns_none(self):
        self.assertIsNone(self.map.get("nonexistent"))

    def test_remove_existing_key(self):
        self.map.put("banana", 7)
        self.map.remove("banana")
        self.assertIsNone(self.map.get("banana"))

    def test_multiple_keys(self):
        self.map.put("a", 1)
        self.map.put("b", 2)
        self.map.put("c", 3)
        self.assertEqual(self.map.get("a"), 1)
        self.assertEqual(self.map.get("b"), 2)
        self.assertEqual(self.map.get("c"), 3)
    
    def test_initial_size_is_zero(self):
        self.assertEqual(self.map.size(), 0)

    def test_size_increases_on_put(self):
        self.map.put("a", 1)
        self.map.put("b", 2)
        self.assertEqual(self.map.size(), 2)

    def test_size_does_not_increase_on_overwrite(self):
        self.map.put("a", 1)
        self.map.put("a", 2)  # Same key
        self.assertEqual(self.map.size(), 1)

    def test_size_decreases_on_remove(self):
        self.map.put("x", 100)
        self.map.put("y", 200)
        self.map.remove("x")
        self.assertEqual(self.map.size(), 1)

    def test_capacity_initial_value(self):
        cap = self.map.capacity()
        self.assertIsInstance(cap, int)
        self.assertGreater(cap, 0)

    def test_resize_doubles_capacity(self):
        old_capacity = self.map.capacity()
        self.map.resize()
        self.assertEqual(self.map.capacity(), old_capacity * 2)

    def test_resize_preserves_all_items(self):
        items = {
            "apple": 1,
            "banana": 2,
            "carrot": 3,
            "date": 4
        }
        for k, v in items.items():
            self.map.put(k, v)

        self.map.resize()

        for k, v in items.items():
            self.assertEqual(self.map.get(k), v)

        self.assertEqual(self.map.size(), len(items))

    def test_resize_and_remove_stability(self):
        self.map.put("key1", 100)
        self.map.put("key2", 200)
        self.map.resize()
        self.map.remove("key1")
        self.assertIsNone(self.map.get("key1"))
        self.assertEqual(self.map.get("key2"), 200)
        self.assertEqual(self.map.size(), 1)

if __name__ == '__main__':
    unittest.main()
