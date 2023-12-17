import unittest
from fonction import generateModele

class Testing(unittest.TestCase):
    def test_model(self):
        self.assertEqual(generateModele(),1)

if __name__ == '__main__':
    unittest.main()