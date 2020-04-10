// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

// Example:

// Input: [-2,1,-3,4,-1,2,1,-5,4],
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.
// Follow up:

// If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


public class Solution {
    public int MaxSubArray(int[] nums) {
        int maxSoFar, currentMax;
        maxSoFar = currentMax = nums[0];
        
        for(int i = 1; i < nums.Length; i++) {
            currentMax = Math.Max(nums[i], currentMax+nums[i])         ;
            maxSoFar = Math.Max(maxSoFar, currentMax);
        }
        return maxSoFar;
    }
}