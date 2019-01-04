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

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        # length of longest possible substring w/o repetion is the number of unique elements
        unique = len(set(s))
        # test all substring from the highest possible length, to 1
        for i in range(unique, 0, -1):
        	# get all substrings of length i
             substrings = [s[a:b] for a, b in zip(range(0, length), range(i, length + 1))]
             # check if a substring does not contain repetition
             for sub in substrings:
             	# substring does not contain repetition, return its length (i)
             	if len(set(sub)) == len(sub):
             		return i
        # if above did not return, empty string was given
        return 0

# test
test_cases = [("abcabcbb",3), ("bbbbb",1), ("pwwkew",3), ("dvdf",3), ("dvabcdef",7), ("aaaaab",2), ("baaaaa",2), ("aaabcaaa",3), ("aaaabacaaa",3), ("",0), (" ",1), ("a",1)]
for tin, tout in test_cases:
	out = Solution.lengthOfLongestSubstring(Solution, tin)
	if out != tout:
		print("Failed! input:{} expected: {} output: {}".format(tin, tout, out))

print(Solution.lengthOfLongestSubstring(Solution, "bpiwuqzdzubdubzvafspqpqwuzifwovyddwyvvburczmgyjgfdxvtnunneslsplwuiupfxlzbknhkwppanltcfirjcddsozoyveg"))
print(Solution.lengthOfLongestSubstring(Solution, "qthepvzhouiriqnqjpgwabpwwoqebcguxnankzwztgsdwgwixcexfwvemliqpomnemcolypfgikfognnktkqrhueteukvgzb"))