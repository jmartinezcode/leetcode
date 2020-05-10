# Given a positive integer num, write a function which returns True 
# if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 14
# Output: false

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i * i <= num:        
            if i * i == num:
                return True
            else:
                i += 1
        return False

    def isPerfectSquare2(self, num):
        if num < 2:
            return True
        
        left, right = 2, num // 2
        while left <= right:
            mid = (left + right) // 2 
            
            if mid*mid == num:
                return True
            elif mid*mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return True