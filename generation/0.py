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
    
    def test_is_palindrome(self):
        self.assertTrue(self.solution('A man, a plan, a canal: Panama'))
        self.assertFalse(self.solution('race a car'))
        self.assertTrue(self.solution('Was it a car or a cat I saw?'))
        
if __name__ == '__main__':
    unittest.main()
    
# Output:
#....
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
```

In the above example, we have defined a test case `test` that inherits from `unittest.TestCase`. We have defined a setUp method that initializes the `is_palindrome` function and a tearDown method that does nothing. We have also