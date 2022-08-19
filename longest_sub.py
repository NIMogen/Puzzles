"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
def longest_sub(s: str) -> int:
    longest_substring = ""
    substring = ""
    for ch in s:
        if ch not in substring and ch not in longest_substring:
            substring += ch
        else:
            if len(substring) > len(longest_substring):
                longest_substring = substring
                subtring = ""
    return len(longest_substring)
            
        
print(longest_sub("abcabcbb"))
print(longest_sub("bbbbb"))
print(longest_sub("pwwkew"))
