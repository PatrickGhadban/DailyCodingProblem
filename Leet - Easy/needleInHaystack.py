'''
* Difficulty: Easy
* Asked by: FAANG (I was asked by Amazon the same question in the final round, except they also wanted all indexes, not just the 1st)
* Problem: Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
           Return 0 if the needle is empty
Example 1:
    Input: haystack = "hello", needle = "ll"
    Output: 2

Example 2:
    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

Time Taken: Originally it was ~10mins
RunTime: O(n)
Space Complexity: O(m)

Description: Use KMP Search Algorithm. This algo has a RunTime of O(n) because it records a matching of a prefix and suffix in the
    substring. And on the instance of a mismatch in chars between the main string and the substring, it resets the index that is iterating
    through the substring to the index of the prefix given on the table

    1.) Loop through the substring and record where there is a match of prefix and suffix.
        EX: d s g w a d s g z
            0 0 0 0 0 1 2 3 0
    2.)
'''

def solution(haystack, needle):
    if len(needle) == 0:
        return 0
    if len(haystack) == 0:
        return -1
    if len(needle) > len(haystack):
        return -1

    # Create matching table
    match_suf_pref = [0] * len(needle)
    k = 0
    for i in range(1, len(needle)):
        k = match_suf_pref[i - 1]
        while needle[k] != needle[i] and k:
            k -= 1
            # k = match_suf_pref[k - 1]
        if needle[k] == needle[i]:
            match_suf_pref[i] = k + 1


    # Find index location of substring in Haystack
    i = j = 0
    # while i < len(haystack) and j < len(needle):
    while i < len(haystack):
        if haystack[i] != needle[j]:
            if j == 0:
                i += 1
            else:
                j = match_suf_pref[j - 1]
        else:
            i += 1
            j += 1
            if j == len(needle):
                return i - j
                # If we were looking for all instanes instead of just the first
                j = match_suf_pref[j - 1]

    return -1


def main():
    print(solution("hello", "ll"))
    print(solution("123", "4"))
    print(solution("suh dude", ""))

if __name__ == "__main__":
    main()
