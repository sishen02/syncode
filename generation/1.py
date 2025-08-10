import unittest

# three test cases for is_palindrome function
class test(unittest.TestCase):
    def setUp(self):
        def is_palindrome(s: str) -> bool:
            '''test whether a string is a palindrome'''
            cleaned = ''.join(filter(str.isalnum, s)).lower()
            return cleaned == cleaned[::-1]
        self.solution = is_palindrome
    
    def tearDown(self):
        pass
    
    def test_palindrome(self):
        self.assertTrue(self.solution("racecar"))
        self.assertTrue(self.solution("A man, a plan, a canal, Panama!"))
        self.assertFalse(self.solution("hello"))
        
# four test cases for is_palindrome function
class test2(unittest.TestCase):
    def setUp(self):
        def is_palindrome(s: str) -> bool:
            '''test whether a string is a palindrome'''
            cleaned = ''.join(filter(str.isalnum, s)).lower()
            return cleaned == cleaned[::-1]
        self.solution = is_palindrome
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
    
