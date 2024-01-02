class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_amount = 0

        left, right = 0, len(height)-1

        while left != right:
            # calculate current amount
            distance = right - left
            smaller_height = min(height[left], height[right])
            current_amount = smaller_height * distance

            # set new max amount
            max_amount = max(max_amount, current_amount)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_amount
    
sol = Solution()
assert sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert sol.maxArea([1,1]) == 1
print("Passed")