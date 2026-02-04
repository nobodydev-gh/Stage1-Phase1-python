import unit_testing
import unittest 

class TestCalc(unittest.TestCase):

    def test_add(self):
        result=unit_testing.add(10,5)
        self.assertEqual(unit_testing.add(10,5),15)






if __name__ == '__main__':
    unittest.main()