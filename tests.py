import unittest
from shop import shop

class CheckoutTests(unittest.TestCase):

    def setUp(self):
        self._shop = shop.Shop()
        self.assertTrue(self._shop)

    def test_outputs(self):
        self.assertEqual(self._shop.checkout('aBc'), -1)
        self.assertEqual(self._shop.checkout('-B8x'), -1)
        self.assertEqual(self._shop.checkout(18), -1)
        self.assertEqual(self._shop.checkout('AA'), 100)
        self.assertEqual(self._shop.checkout('ABCD'), 115)
        self.assertEqual(self._shop.checkout('AAA'), 130)
        self.assertEqual(self._shop.checkout('AAAAAA'), 260)
        self.assertEqual(self._shop.checkout('ABBABABACBA'), (130+100+90+30+20))

if __name__ == "__main__":
    unittest.main()
