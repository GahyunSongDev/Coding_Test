# Coding_Test
## Remove Element

### Description
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

### Solution
1) 첫번 째 솔루션 (slicing + sorted + set)
```python
class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums))
        return len(nums)
```
=> nums 의 array list 를 set로 바꾼 이유 : set는 중복 되는 요소를 허용하지 않는 자료형이므로, 즁복되는 요소들을 제거해 줌.
=> nums = sorted(set(nums))로 하지 않은 이유 : 
    "nums[:]"로 슬라이싱을 사용하여 리스트를 새로 만들지 않고 리스트의 요소를 직접 수정한다 왜냐하면 리스트를 수정해야하는 것("In-Place")이 이 문제에서 원하는 바이기 떄문에이다. "nums[:]"로 슬라이싱은 입력 배열을 수정하는 데 사용되는 메모리가 상수로 유지되기 때문에 공간 복잡도(space complexcity) = O(1). 만약 "nums = " 으로 했다면 새로운 리슽트를 만들기 떄문에 공간 복잡도(space complexcity) = O(N) 이 된다.
=> 시간 복잡도(Time Complexcity) = O(n log n)

2) 두번쨰 솔루션 (Two-pointers with for-loop)
```python
class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
		j = 0
		for i in range(1, len(nums)):
			if nums[j] != nums[i]:
				j += 1
				nums[j] = nums[i]
		return j + 1
```

        
3) 세번째 솔루션 (using .pop() with while-loop)
```python
class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
		def removeDuplicates(self, nums: List[int]) -> int:
		i = 1
		while i < len(nums):
			if nums[i] == nums[i - 1]:
				nums.pop(i)
			else:
				i += 1
		return len(nums)
```