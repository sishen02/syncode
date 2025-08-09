import unittest

# three test cases for maximal profit problem
class test(unittest.TestCase):
    def setUp(self):
        def solution(prices):
            min_price = float('inf')
            max_profit = 0
            for price in prices:
                if price < min_price:
                    min_price = price
                elif price - min_price > max_profit:
                    max_profit = price - min_price
            return max_profit
        self.solution = solution
    
    def tearDown(self):
        pass
    
    def test_case_1(self):
        prices = [7,1,5,3,6,4]
        self.assertEqual(self.solution(prices), 5)
    
    def test_case_2(self):
        prices = [7,6,4,3,1]
        self.assertEqual(self.solution(prices), 0)
    
    def test_case_3(self):
        prices = [1,2,3,4,5]
        self.assertEqual(self.solution(prices), 4)
        
if __name__ == '__main__':
    unittest.main()
    
# Output:
#....
#....
#....
#....
#....
#....
#