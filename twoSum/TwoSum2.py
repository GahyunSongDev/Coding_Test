class Solution(object):
    def twoSum(self, nums, target):
        dicOfnums = {}
        i = 0

        for i in range(len(nums)):
            # put the keys and values into the dictionary with nums inputs. key : the element of the nums, value : the index of the element
            dicOfnums[nums[i]] = i

        # another for loop to print the indexes of the tartget
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dicOfnums and i != dicOfnums[comp]:
                return [i, dicOfnums[comp]]

solution = Solution()

result = solution.twoSum(nums = [3,2,4], target = 6)
print(result)