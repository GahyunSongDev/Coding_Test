class Solution(object):
    def isValid(self, s):
        Stack = []
        map_brackets = {')' : '(', ']' : '[', '}' : '{'}

        for i in s :
            if i in map_brackets.values() :
                Stack.append(i)
            elif i in map_brackets.keys() :
                if not Stack or map_brackets[i] != Stack.pop():
                    return False
            else :
                return False
        return not Stack
    
# Test
solution = Solution()

#Test cases
test_cases = {
    "Test 1": ("[()(())((()))]", True),
    "Test 2": ("{[()]}", True),
    "Test 3": ("({[}])", False),
    "Test 4": ("", True),
    "Test 5": ("[", False),
    "Test 6": ("]", False),
    "Test 7": ("[({})]", True),
    "Test 8": ("[({})](]", False)
}

# Running the tests
for name, (input_str, expected) in test_cases.items():
    result = solution.isValid(input_str)
    print(f"{name} - Input: {input_str} | Expected: {expected} | Result: {result} | Passed: {result == expected}")
