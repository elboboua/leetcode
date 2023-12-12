class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        paren_stack = []

        for char in s:
            if char in paren_dict:
                if paren_stack and paren_stack[-1] == paren_dict[char]:
                    paren_stack.pop()
                else:
                    return False
            else:
                paren_stack.append(char) 

        return len(paren_stack) == 0
    
sol = Solution()

s = "()"
assert sol.isValid(s) == True


s = "()[]{}"
assert sol.isValid(s) == True


s = "(]"
assert sol.isValid(s) == False
print("Passed")