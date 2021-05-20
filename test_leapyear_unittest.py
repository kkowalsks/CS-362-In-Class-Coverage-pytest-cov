import unittest
import leapyear

class testCaseLeapCheck(unittest.testCase):
    def test_leapCheck(self):
        self.assertEqual(leapyear.leapCheck(2008), True)
        self.assertEqual(leapyear.leapCheck(2100), False)
        self.assertEqual(leapyear.leapCheck(2000), False)

if __name__ == '__main__':
    unittest.main()