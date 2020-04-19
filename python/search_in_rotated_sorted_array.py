# Suppose an array sorted in ascending order is rotated at some pivot 
# unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. 
# If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

#BST recursive solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, len(nums) - 1)
    
    def helper(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1
        middle = (left + right) // 2
        possible_match = nums[middle]
        if target == possible_match:
            return middle
        elif nums[left] <= possible_match:
            if target < possible_match and target >= nums[left]:
                return self.helper(nums, target, left, middle - 1)
            else:
                return self.helper(nums, target, middle + 1, right)
        else:
            if target > possible_match and target <= nums[right]:
                return self.helper(nums, target, middle + 1, right)
            else:
                return self.helper(nums, target, left, middle - 1)

    