import sys
sys.path.append("..")
from utils.display_test import display_test_header, display_test_results

class Solution():
    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        # return two indices of numbers that add up to target
        return_nums = []
        left, right = 0, len(numbers)-1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left, right]
            elif sum < target:
                left += 1
            else:
                right -= 1

        return return_nums
    
cases = [
    [[[1,2,3,4,5], 50], []], 
    [[[1,2,3,4,10], 6], [1,3]]
]
sol = Solution()

display_test_header("167 - Two Sum II")
for i, case in enumerate(cases):
    args, correct_res = case

    res = sol.two_sum(*args)
    assert res == correct_res
    print(f"Passed test #{i}")
