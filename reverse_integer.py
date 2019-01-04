'''
Reverse Integer
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string_int = str(x)
        multiplier = 1
        if x < 0:
            multiplier = -1
            string_int = string_int[1:]
        reversed = multiplier * int("".join([string_int[i] for i in range(len(string_int) - 1, -1, -1)]))
        if reversed < -2147483648 or reversed > 2147483647:
            return 0
        return reversed
