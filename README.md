# Leetcode Live Solution Finder
Run the script during an coding interview. The script will parse your speech input, and show you the solution to the most similar leetcode question from Blind75. 
## In Action
```
Transcribed text: design a data structure that supports adding new words and finding if a string matches any previously added string
The most similar question is:  longest palindromic substring - given a string s, return the longest palindromic substring in s.
The most similar question name is:  Longest Palindromic Substring
The match score is:  0.38095238095238093
The solution code is:
class Solution:
    def helper(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j - i - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            temp = max(self.helper(s, i, i), self.helper(s, i, i + 1))     
            if temp > end - start:
                start = i - (temp - 1) // 2
                end = i + temp // 2
        return s[start:end + 1]
waiting for speech...
waiting for speech...
waiting for speech...
Transcribed text: if you choose any character of the string and change it to any other uppercase english character
The most similar question is:  longest repeating character replacement - you are given a string s and an integer k. you can choose any character of the string and change it to any other uppercase english character. you can perform this operation at most k times.

return the length of the longest substring containing the same letter you can get after performing the above operations.
The most similar question name is:  Longest Repeating Character ReplacementThe match score is:  0.42316258351893093
The solution code is:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, max_repeat = 0, 0
        freq = {}
        if len(s) <= k:
            return len(s)
        l = 0
        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1
            max_repeat = max(max_repeat, freq[s[r]])
            if r - l + 1 - max_repeat > k:
                freq[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)
        return ans
```

## Data Source
Blind 75 list and solution source: https://github.com/wk16/Leetcode-Blind-75/tree/main/PythonSolutions
