class Solution(object):
    def twoSum(self, nums, target):
        len_nums = len(nums)
        for i in range (len_nums-1):
            for j in range(i+1, len_nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
solution = Solution()

result = solution.twoSum(nums = [3,2,4], target = 6)
print(result)