class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        t_sum = 0
        for i in range(len(nums)):
            t_sum +=nums[i]
            
        ac_sum = l*(l+1) /2
        
        return int(ac_sum - t_sum)