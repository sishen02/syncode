from syncode import Syncode
import subprocess

import warnings
warnings.filterwarnings("ignore")

models = ['microsoft/phi-2', 'microsoft/phi-1', 'Salesforce/codegen-350M-nl']

for i, model in enumerate(models):
    print(f"Model: {model} Start Generating")
    syn_llm = Syncode(model=model, grammar='./python_unittest.lark', parse_output_only=False, indent=True, max_new_tokens=200)
    prefix = """import unittest

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
    
"""
    output = syn_llm.infer(prefix)[0]
    program = prefix + output
    print(program)
    print()
    with open(f'generation/{i}.py', 'w') as f:
        f.write(program)

for i, model in enumerate(models):
    try:
        print(f"Model: {model} Start Testing")
        subprocess.run(
            ['coverage', 'run', f'generation/{i}.py']
        )
        subprocess.run(
            ['coverage', 'report']
        )
    except Exception as e:
        print("Error running tests")
        print(f"Model: {model}")
        print(e)