'''
* Difficulty: Easy
* Asked by: FAANG, IBM, VISA, Oracle
* Problem: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

EXAMPLES:
Input: "()[]{}"             Input: "{[]}"               Input: "([)]"
Output: true                Output: true                Output: false

Time Taken: 20mins
RunTime: O(n)
Space Complexity: O(1)

Description:
    1.) Base Cases:
        a.) Check if string is empty
        * b.) Check if the string is of an odd length. Reason being, valid parenthesis must be pairs.
    2.) Iterate through the string.
    3.) Check if the bracket is an open bracket. If so, push to stack.
    4.) If not, pop from the stack and check if the closed bracket is a pair to the popped open bracket. If not, return False
    5.) Lastly, a base case, if only open brackets were part of the string, the stack would not be empty, which means
        there would not be a closed bracket for evey open bracket.
'''

def validParenthesis(s):
    if len(s) == 0:
        return True
    if len(s) % 2 != 0:
        return False

    bracket_pairs = {'(' : ')' , '{' : '}' , '[' : ']'}
    seen = []

    for bracket in s:
        if bracket in bracket_pairs.keys():
            seen.append(bracket)
        else:
            if len(seen):
                seen_open_bracket = seen.pop()
                if bracket != bracket_pairs[seen_open_bracket]:
                    return False
    if len(seen):
        return False
    return True


def main():
    print(validParenthesis("()[]{}"))
    print(validParenthesis("{[]}"))
    print(validParenthesis("(["))

if __name__ == "__main__":
    main()
