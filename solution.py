class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        total_sum=sum(nums)
        running_sum=0

        for i in range(len(nums)):
            running_sum += nums[i]
            if(total_sum == running_sum):
                return i
            total_sum -= nums[i]
        return -1
