class Solution:
    def selection_sort(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            smallest = i
            for j in range(i+1, len(nums)):
                if nums[smallest] > nums[j]:
                    smallest = j
            nums[i], nums[smallest] = nums[smallest], nums[i]

        return nums
    

sol = Solution()
arr = [6, 4, 3, 1, 100, -340]
assert sol.selection_sort(arr) == sorted(arr)
print("passed")
