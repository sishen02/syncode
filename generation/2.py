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
        self.solution = solution
    
    def test_max_profit(self):
        self.assertEqual(self.solution(1.0), 1.0)
        self.assertEqual(self.solution(1.0), 1.0)
        self.assertEqual(self.solution(1.0), 1.0)
        self.assertEqual(self.solution(1.0), 1.0)
        self.assertEqual(self.solution(1.0), 1.0)
        self.assertEqual(self.solution(1.0), 1