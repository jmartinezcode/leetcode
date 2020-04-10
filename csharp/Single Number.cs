// Given a non-empty array of integers, every element appears twice except for one. Find that single one.

// Note:

// Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

// Example 1:

// Input: [2,2,1]
// Output: 1
// Example 2:

// Input: [4,1,2,1,2]
// Output: 4

// Time complexity : O(n). Time complexity of for loop is O(n). Time complexity of hash table(dictionary in python/C#) operation pop is O(1).

// Space complexity : O(n). The space required by hashtable is equal to the number of elements in nums.


public class Solution {
    public int SingleNumber(int[] nums) {
        Dictionary<int,int> test = new Dictionary<int,int>();
        long sum1 = 0, sum2=0;
        for (int i = 0; i < nums.Length; i++){
            if (!test.ContainsKey(nums[i])) {
                sum1 += nums[i];
                test.Add(nums[i], 1);
            }
            sum2 += nums[i];
        }
        return (int)(2 * (sum1) - sum2);
    }
}