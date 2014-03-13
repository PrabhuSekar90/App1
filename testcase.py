import unittest
import test1
class Test_csvValue(unittest.TestCase):
    
    def test_outputValCheck(self):            
        objNumUtils = test1._test1()   
        self.assertEqual(objNumUtils.result_data('C:/Users/SNTAdmin/Desktop/test.csv'), [(228.0, '1990', 'feb', 'company 1'), (245.0, '1990', 'jan', 'company 2'), (243.0, '1990', 'jan', 'company 3')])
if __name__ == '__main__':
    unittest.main()
