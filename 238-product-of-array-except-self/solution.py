from typing import List


class Solution:
    # Brute Force: O(n^2)
    def product_of_array_except_self_brute_force(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i == j:
                    continue
                ans[j] *= nums[i]

        return ans

    # Efficient: O(3n) -> O(n)
    def product_of_array_except_self_efficient(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                prefix[i] = nums[i]
                continue
            prefix[i] = prefix[i - 1] * nums[i]

        postfix = [1] * len(nums)
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                postfix[j] = nums[j]
                continue
            postfix[j] = postfix[j + 1] * nums[j]

        ans = [1] * len(nums)
        for x in range(0, len(nums)):
            if x == 0:
                ans[x] = 1 * postfix[x + 1]
            elif x == len(nums) - 1:
                ans[x] = prefix[x - 1] * 1
            else:
                ans[x] = prefix[x - 1] * postfix[x + 1]

        return ans

    # Most efficient: O(1) in space, O(n) in time (if you do not count the array creation, rule per leetcode)
    def product_of_array_except_self_most_efficient(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefix = 1
        for i in range(0, len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output


tests = [[[1, 3, 4, 5], [60, 20, 15, 12]]]

sol = Solution()

for case in tests:
    nums, solution = case
    assert (
        sol.product_of_array_except_self_brute_force(nums) == solution
    ), f"brute force: {nums} should output {solution}"
    assert (
        sol.product_of_array_except_self_efficient(nums) == solution
    ), f"efficient: {nums} should output {solution}"
    assert (
        sol.product_of_array_except_self_most_efficient(nums) == solution
    ), f"most efficient: {nums} should output {solution}"
