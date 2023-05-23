from typing import List
class Solution:
    # O(n^2) time complexity
    def contains_duplicate_brute_force(self, nums: List[int]) -> bool:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False
    
    # O(n) time complexity
    def contains_duplicate_efficient(self, nums: List[int]) -> bool:
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        for _ , v in mp.items():
            if v > 1:
                return True
            
        return False
    
    # O(n) time complexity. The creation of the set is O(n)
    def contains_duplicate_using_set(self, nums: List[int]) -> bool:
        s = set(nums)
        return True if len(s) != len(nums) else False

tests = [[[1, 3, 4, 5], False], [[1,2,2,4], True], [[], False]]

sol = Solution()

for case in tests:
    nums, result = case
    assert sol.contains_duplicate_brute_force(nums) == result
    assert sol.contains_duplicate_efficient(nums) == result
    assert sol.contains_duplicate_using_set(nums) == result