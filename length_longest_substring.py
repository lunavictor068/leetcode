'''
Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        for i in range(length, 0, -1):
             substrings = [s[a:b] for a, b in zip(range(0, length), range(i, length + 1))]
             for sub in substrings:
             	if len(set(sub)) == len(sub):
             		return i
        return 0

test_cases = [("abcabcbb",3), ("bbbbb",1), ("pwwkew",3), ("dvdf",3), ("dvabcdef",7), ("aaaaab",2), ("baaaaa",2), ("aaabcaaa",3), ("aaaabacaaa",3), ("",0), (" ",1), ("a",1)]
for tin, tout in test_cases:
	out = Solution.lengthOfLongestSubstring(Solution, tin)
	if out != tout:
		print("Failed! input:{} expected: {} output: {}".format(tin, tout, out))

print(Solution.lengthOfLongestSubstring(Solution, "bpiwuqzdzubdubzvafspqpqwuzifwovyddwyvvburczmgyjgfdxvtnunneslsplwuiupfxlzbknhkwppanltcfirjcddsozoyveg"))
print(Solution.lengthOfLongestSubstring(Solution, "qthepvzhouiriqnqjpgwabpwwoqebcguxnankzwztgsdwgwixcexfwvemliqpomnemcolypfgikfognnktkqrhueteukvgzb"))