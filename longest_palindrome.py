'''
Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if s == "":
    	return s
    for l in range(len(s), 0, -1):
    	for i in range(l, len(s) + 1, 1):
    		sub_str = s[i-l:i]
    		if is_palindrome(sub_str):
    			return sub_str


def is_palindrome(string):
    length = len(string)
    for a, b in zip(range(0, length - 1, 1), range(length - 1, -1, -1)):
        if a >= b:
            break
        if string[a] != string[b]:
            return False
    return True


print(longestPalindrome("racecar"))
print(longestPalindrome("r"))
print(longestPalindrome("njs,mdakjsjdfsjkracecari82ms82mjnioyuisd"))
print(longestPalindrome("babad"))

