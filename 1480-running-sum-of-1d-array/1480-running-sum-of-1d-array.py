class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        results= []
        results.append(nums[0])
        for i in range(1,len(nums)):
            results.append(nums[i]+results[i-1])
        return results