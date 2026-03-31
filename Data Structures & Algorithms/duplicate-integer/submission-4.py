class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) != len(set(nums)):
        #     return True
        # else:
        #     return False
        return True if len(nums) > len(set(nums)) else False
        