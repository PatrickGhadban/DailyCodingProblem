'''
* Difficulty: Easy
* Asked by:
* Problem: Palindrom of a number
Example 1:          Example2:               Example3:
  Input: 121          Input: -123             Input: 120
  Output: True        Output: False           Output: False

Time Taken: > 10mins
RunTime: O(logn)
Space Complexity: O(1)

Description:
1.) Check if x is neg;  return False is so
2.) Set rev = reverse the integer
3.) If X == rev return True
'''



def isPalindrome(x):
    if x < 0:
        return False

    rev = reverse_int(x)

    if rev == x:
        return True
    else:
        return False

def reverse_int(x):
    rev = 0
    while x:
        pop = x % 10
        x = x // 10
        rev = rev * 10 + pop
    return rev


def main():
    print (isPalindrome(121))
    print (isPalindrome(0))
    print (isPalindrome(120))
    print (isPalindrome(-121))

if __name__ == "__main__":
    main()
