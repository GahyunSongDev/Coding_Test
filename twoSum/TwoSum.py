class Solution(object):
    # 1) Brute force

    # def twoSum(self, nums, target):
    #     len_nums = len(nums)
    #     for i in range (len_nums-1):
    #         for j in range(i+1, len_nums):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    #2) Two Pointer
    def twoSum(self, nums, target):
        # Create a new hash table having values and keys of nums input array.
        indices = {}
        for i in range (len(nums)):
            indices[nums[i]] = i
    
        # check if there's a complement in the hash table and the value of the key with the complement is not equal to i
        # if the value of the key with the hash table is not equal i, it return a list containing the current index i and the index of the complement stored in the indices dictionary
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in indices and indices[complement] != i:
                return [i, indices[complement]]

solution = Solution()

result = solution.twoSum(nums = [3,2,4], target = 6)
print(result)