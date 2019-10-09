'''
* Difficulty: Medium
* Asked by: FAANG, Oracle, IBM, Mathworks
* Problem: You are given two non-empty linked lists representing two non-negative integers.
           The digits are stored in reverse order and each of their nodes contain a single digit.
           Add the two numbers and return it as a linked list.
           NOTE: You may assume the two numbers do not contain any leading zero, except the number 0 itself.

EXAMPLE:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

Time Taken: 40mins
RunTime: O(max(l1, l2))
Space Complexity: O(max(l1, l2))

Description: Essentially, you're just doing simple addition but left->right.
    1.) Declare a variable to hold the "carry" for sums that are greater than 9
        Declare the new linkedlist dummy head and a new "next" variable equal to it
    2.) While there are still numbers left in l1 or l2 or there is still a number carried over from the last iteration. loop through
    3.) Add the values at each index of the linkedlist
    4.) Divide the sum by 10 and set carry to the remainder
    5.) Add the remainder (val) to the new linkedlist
'''

def addTwo(l1, l2):
    carry = 0
    rootNode = ListNode(-1)
    sumTotal = rootNode
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        carry, val = divmod(carry, 10)
        sumTotal.next = ListNode(val)
        sumTotal = sumTotal.next
    return rootNode.next


def main():
    print(addTwo())
    print(addTwo())

if __name__ == "__main__":
    main()
