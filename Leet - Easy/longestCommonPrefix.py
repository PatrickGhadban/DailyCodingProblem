'''
* Difficulty: Easy
* Asked by: Amazon, Quora, (6-12months back: Google, FB, Apple, Adobe)
* Problem: Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
EXAMPLE:
    Input: ["flower","flow","flight"]
    Output: "fl"


Time Taken: 20mins
RunTime: O(S) where S is the length of all characters in the list.
Space Complexity: O(1)

Description:
    1.) Find the word with the smallest length in the list and set it equal to 'lcp'
    2.) Iterate through the enumerate 'lcp' -> NOTE: enumerate return [(index, value), ...]
    3.) Loop through every word in the list and check if the lcp char matches the char of the word at the same index of the 'lcp'
    4.) When the char of the word and of the 'lcp' don't match, you've found the longest common prefix
'''

def longestCommonPrefix(lst):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]

    lcp = min(strs, key=len)

    for i, char in enumerate(lcp):
        for word in strs:
            if word[i] != char:
                return lcp[:i]
    return lcp



def main():
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))

if __name__ == "__main__":
    main()
