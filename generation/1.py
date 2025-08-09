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
    
    def test_max_profit(self):
        self.assertEqual(self.solution([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(self.solution([7, 6, 4, 3, 1]), 0)
        self.assertEqual(self.solution([1, 2, 3, 4, 5]), 4)
        self.assertEqual(self.solution([1]), 0)
        
if __name__ == '__main__':
    unittest.main()
