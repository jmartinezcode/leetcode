// Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

// Example 1:

// Input: S = "ab#c", T = "ad#c"
// Output: true
// Explanation: Both S and T become "ac".
// Example 2:

// Input: S = "ab##", T = "c#d#"
// Output: true
// Explanation: Both S and T become "".
// Example 3:

// Input: S = "a##c", T = "#a#c"
// Output: true
// Explanation: Both S and T become "c".
// Example 4:

// Input: S = "a#c", T = "b"
// Output: false
// Explanation: S becomes "c" while T becomes "b".
// Note:

// 1 <= S.length <= 200
// 1 <= T.length <= 200
// S and T only contain lowercase letters and '#' characters.
// Follow up:

// Can you solve it in O(N) time and O(1) space?

public class Solution {
  public bool BackspaceCompare(string S, string T) {
    int S_pointer = S.Length - 1;
    int T_pointer = T.Length - 1;
    int S_skips = 0;
    int T_skips = 0;
    
    while (S_pointer >= 0 || T_pointer >= 0) {
        
      while (S_pointer >= 0) {
        if (S[S_pointer] == '#') {
          S_skips++;
          S_pointer--;
        } else if (S_skips > 0) {
          S_pointer --;
          S_skips --;
        } else {
          break;
        }
      }                
      while (T_pointer >= 0) {
        if (T[T_pointer] == '#') {
          T_skips++;
          T_pointer--;
        } else if (T_skips > 0) {
          T_pointer--;
          T_skips--;
        } else {
          break;
        }
      } 
      if (S_pointer >= 0 && T_pointer >= 0 && S[S_pointer] != T[T_pointer]) {
        return false;
      }
      if ((S_pointer >= 0) != (T_pointer >= 0)) {
        return false;
      }
      S_pointer--;
      T_pointer--;
    }   
    return true;
  }
}