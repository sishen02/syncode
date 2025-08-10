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
        self.solution = None
    
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome(self.solution), True)
    
    def test_is_palindrome_with_empty_string(self):
        self.assertEqual(is_palindrome(self.solution), False)
    
    def test_is_palindrome_with_empty_string_with_empty_string(self):
        self.assertEqual(is_palindrome(self.solution), False)
    
    def test_is_palindrome_