'''
* Difficulty: Easy
* Asked by:
* Problem: Given a 32-bit signed integer, reverse digits of an integer.
Example 1:          Example2:               Example3:
  Input: 123          Input: -123             Input: 120
  Output: 321         Output: -321            Output: 21

Time Taken: 25mins
RunTime: O(logn)
Space Complexity: O(1)

Description:
1.) Check if x is a 32-bit integer
2.) Reverse the integer
    a.) Get any negative x to a positive
    b.) "Pop" the end of the int by taking the mod
    c.) Divide the positve x by 10 (NOTE: '//' divides and rounds down )
    d.) Multiply the result by 10 and add (or push) the remainder
3.) Check if teh result is a 32-bit integer.
'''


def rev_int(x):
    # Check if x is 32-bit int
    if x >= 2**31 - 1 or x <= -2**31:
        return 0

    res = 0
    pos_x = abs(x)
    while pos_x != 0:
        # pop off the remainder of the int:
        pop = pos_x % 10
        pos_x = pos_x // 10
        # push the remainder the end of the reversed int:
        res = res * 10 + pop

    # If x was originally neg, return the sign to the result
    if x < 0:
        res = res * -1

    # Check if result is 32-bit int
    if res >= 2**31 - 1 or res <= -2**31:
        return 0

    return res


def main():
    print (rev_int(123))
    print (rev_int(-123))
    print (rev_int(120))

if __name__ == "__main__":
    main()
