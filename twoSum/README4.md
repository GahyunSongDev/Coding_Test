# Coding Test
## Two Sum (First Try)

### Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 10^4
-109 <= nums[i] <= 10^9
-109 <= target <= 10^9
Only one valid answer exists.

### Solution

< The ways to approach this problem >

1) Brute Force (완전탐색)
    The timecomplex is O(n^2), which fit to the first constraint "2 <= nums.length <= 10^4".
2) hasg table (해쉬테이블)
    The implementation efficiently solves the Two Sum problem using the two-pointer technique and a hash table to achieve a time complexity of O(n), where n is the number of elements in the nums array. This is because both building the hash table and finding the complement involve iterating through the array once, leading to linear time complexity.
<br/>
---------------------------------------------------------------------------------------------------
<br/>

[ 1. Two Sum ] - Second Try

