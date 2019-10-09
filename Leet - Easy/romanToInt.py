'''
* Difficulty: Easy
* Asked by: Amazon, FB, Microsoft
* Problem: Converts roman numerals to integers
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Time Taken: 30mins
RunTime: O(n)
Space Complexity: O(1)

Description: This is far from the most elegant solution but it's a conditional heavy problem, so that leads to a lot of if statements
1.) Build a hash map that stores the roman numerals and the corresponding numerical Value
2.) Iterate through the string and check the proceeding char cause a subtraction instance.
    a.) If yes, set value equal to the subtraction and iterate i once
    b.) If no, set value equal to the roman numerals corresponding value
'''

def romanToInt(s):
    conversion = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    answer = 0
    i = 0

        while i < len(s):
            char = s[i]

            if i == len(s) - 1:
                answer = answer + conversion[char]
                break

            if char == 'I':
                if s[i+1] == 'V' or s[i+1] == 'X':
                    value = conversion[s[i+1]] - conversion[char]
                    i += 1
                else:
                    value = conversion[char]
            elif char == 'X':
                if s[i+1] == 'L' or s[i+1] == 'C':
                    value = conversion[s[i+1]] - conversion[char]
                    i += 1
                else:
                    value = conversion[char]
            elif char == 'C':
                if s[i+1] == 'D' or s[i+1] == 'M':
                    value = conversion[s[i+1]] - conversion[char]
                    i += 1
                else:
                    value = conversion[char]
            else:
                value = conversion[char]

            answer = answer + value
            i += 1

        return answer

def main():
    print(romanToInt('XCII'))
    print(romanToInt('XXVII'))
    print(romanToInt('III'))
    print(romanToInt('MDCXVI'))
    print(romanToInt('MCVI'))


if __name__ == "__main__":
    main()
