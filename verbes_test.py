import unittest
import verbes

class TestVerbes(unittest.TestCase):
    def test_is_voyelle(self):
        temp = ['η', 'ώ', 'α']
        for v in temp:
            self.assertTrue(verbes.is_voyelle(v))


if __name__ == '__main__':
    unittest.main()
