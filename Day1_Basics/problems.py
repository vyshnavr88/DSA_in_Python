# 1. Two Sum (https://leetcode.com/problems/two-sum/)
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# 2. Palindrome Number (https://leetcode.com/problems/palindrome-number/)
def isPalindrome(x):
    return str(x) == str(x)[::-1]

# 3. Valid Anagram (https://leetcode.com/problems/valid-anagram/)
def isAnagram(s, t):
    return sorted(s) == sorted(t)