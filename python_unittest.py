from syncode import Syncode
import subprocess

import warnings
warnings.filterwarnings("ignore")

models = ['microsoft/phi-2', 'microsoft/phi-1', 'Salesforce/codegen-350M-nl']

for i, model in enumerate(models):
    print(f"Model: {model} Start Generating")
    syn_llm = Syncode(model=model, grammar='./python_unittest.lark', parse_output_only=False, indent=True, max_new_tokens=200)
    prefix = r"""import unittest

# three test cases for is_palindrome function
class test(unittest.TestCase):
    def setUp(self):
        def is_palindrome(s: str) -> bool:
            '''test whether a string is a palindrome'''
            cleaned = ''.join(filter(str.isalnum, s)).lower()
            return cleaned == cleaned[::-1]
        self.solution = is_palindrome
    
"""
    output = syn_llm.infer(prefix)[0]
    program = prefix + output
    with open(f'generation/{i}.py', 'w') as f:
        f.write(program)

for i, model in enumerate(models):
    try:
        print(f"Model: {model} Start Testing")
        result = subprocess.run(
            ['coverage', 'run', f'generation/{i}.py'],
            capture_output=True,
            text=True
        )
        with open(f'generation/{i}.txt', 'w') as f:
            f.write(f'Model: {model} Test Result\n')
            f.write(result.stderr)
        coverage = subprocess.run(
            ['coverage', 'report'],
            capture_output=True,
            text=True
        )
        with open(f'generation/{i}.txt', 'a') as f:
            f.write(f'Model: {model} Coverage Report\n')
            f.write(coverage.stdout)
    except Exception as e:
        print(f"Model: {model} Error running tests")
        with open(f'generation/{i}.txt', 'w') as f:
            f.write(f'Model: {model} Error running tests\n')
            f.write(e)
