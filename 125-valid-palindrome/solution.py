import sys
sys.path.append("..")
from utils.display_test import display_test_header, display_test_results

class Solution():
    def is_palindrome(self, s) -> bool:
        # remove nonalphanumeric and make everythin lower case
        s_sanitized = [x.lower() for x in s if x.isalnum()]
        return s_sanitized == s_sanitized[::-1]


cases = [[["A man, a plan, a canal: Panama"], True], [["james"], False]]
sol = Solution()


display_test_header("125 - Valid Palindrome")
for case in cases:
    args, correct_res = case

    res = sol.is_palindrome(*args)
    display_test_results(func=sol.is_palindrome, args=args, correct_res=correct_res, res=res)
    assert res == correct_res