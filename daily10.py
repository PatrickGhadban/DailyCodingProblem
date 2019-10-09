'''
* Difficulty: Medium
* Asked by:
* Problem: There are n bulbs that are initially off.
You first turn on all the bulbs.
Then, you turn off every second bulb.
On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on).
For the i-th round, you toggle every i bulb.
For the n-th round, you only toggle the last bulb.
Find how many bulbs are on after n rounds.

EXAMPLE:
Input: 3
Output: 1
Explanation:
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.


Time Taken: 30mins
RunTime: O(1)
Space Complexity: O(1)

Description: First, do a few examples, it's much easier to see the pattern afterwards
n = 4: 1001
n = 6: 100100
n = 9: 100100010
As you can see, every evenly squared number is equal to 1 (or light switch is on) and the end
of the process. Therefore, sqrt(n) will give the number of light(s) left on.
'''

import math

def switch(n):
    # n - the number of bulbs & the number of rounds
    answer = int(math.sqrt(n))
    print (answer)
    return answer

def main():
    switch(1) #1
    switch(6) #2
    switch(9) #3
    switch(12) #3
    switch(16) #4
    switch(20) #4

if __name__ == "__main__":
    main()
