class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            left = i + 1

            while left <= len(nums)-1:
                if num + nums[left] == target:
                    return [i,left]
                left += 1

        return []