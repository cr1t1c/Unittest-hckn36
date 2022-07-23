import unittest
from Frontend import Frontend
import datetime


class firstTest(unittest.TestCase):

    def setup(self):
        self.result = Frontend.frontend()
        

    def test_symbol(self):
        testResult = self.result.ticker.isalpha()
        self.assertEqual(testResult, True)
        pass
        
    
    def chartType_test(self):
        self.assertTrue(1 <= chartType <= 2)
        pass
    
    def timeSeries_test(self):
        self.assertTrue(1 <= timeSeries <= 4)
        pass
    

    def startDate_test(self):
        try:
            datetime.strptime(startDate, '%Y-%m-%d')
            self.assertEqual(startDate, True)
        
        pass

  def endDate_test(self):
        try:
            datetime.strptime(endDate, '%Y-%m-%d')
            self.assertEqual(endDate, True)
        
        pass

if __name__ == "__main__":
    unittest.main()