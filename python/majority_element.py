# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

#Time: O(n)
#Space: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums) 
        return max(count.keys(), key=count.get)


    # Time O(n)
    # Space O(1)
    def majorityElement2(self, nums: List[int]) -> int:
        count = 0
        possible = None

        for num in nums:
            if count == 0:
                possible = num
            count += (1 if num == possible else -1)
        return possible