# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right, answer = [0]*length, [0]*length, [0]*length
        left[0] = 1
        right[-1] = 1

        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]
        for i in reversed(range(length-1)):
            right[i] = nums[i + 1] * right[i + 1]

        for i in range(length):
            answer[i] = left[i] * right[i]

        return answer

    #constant space O(1) solution
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length
        answer[0] = 1

        for i in range(1, length):
            answer[i] = nums[i - 1] * answer [i - 1]
        
        right = 1

        for i in reversed(range(length)):
            answer[i] *= right
            right *= nums[i]

        return answer



