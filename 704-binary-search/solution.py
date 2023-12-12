class Solution:
    def search(self, nums: list[int], target: int) -> int:  
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1

sol = Solution()

nums_1 = [-1,0,3,5,9,12]
target_1 = 9
answer_1 = 4
print(f"Testing {nums_1}, looking for {target_1}. Should be {answer_1}:", sol.search(nums_1, target_1))
assert sol.search(nums_1, target_1) == answer_1

nums_2 = [-1,0,3,5,9,12] 
target_2 = 2
answer_2 = -1
print(f"Testing {nums_2}, looking for {target_2}. Should be {answer_2}:", sol.search(nums_2, target_2))
assert sol.search(nums_2, target_2) == answer_2