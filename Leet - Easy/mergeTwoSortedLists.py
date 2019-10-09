'''
* Difficulty: Easy
* Asked by: FAANG, VISA, Oracle
* Problem: Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

EXAMPLE:
    Input: 1->2->4  ,  1->3->4
    Output: 1->1->2->3->4->4

Time Taken: 25mins
RunTime: O(n + m)
Space Complexity: O(1)

Description:
    1.) Check for empty lists.
    2.) Declare a new Node that will act as a head and will point to the rest of the nodes AND set a variable equal to it.
    3.) Iterate through both lists until one reaches None. During each iteration, compare the current l1, l2 nodes and set the
        new list equal to the smaller node.
    4.) One list will be pointing to None while the other will still have Nodes needed to be added to the list. So,
        point the new list equal to the non-empty list.
    5.) Lastly, return the next of the "preHead" variable. This is because the head was just a placeholder to point to the
        Nodes of the other 2 lists.
'''

def merge(l1, l2):
    # Base Case
    if not l1 and not l2:
        return l1
    if not l1:
        return l2
    if not l2:
        return l1

    # Declare a new list and, set nextNode pointing to said new list
    preHead = ListNode(-1)
    nextNode = preHead

    # Iterate through both lists until one reaches None
    while l1 and l2:
        if l1.val <= l2.val:
            nextNode.next = l1
            l1 = l1.next
        else:
            nextNode.next = l2
            l2 = l2.next
        nextNode = nextNode.next

    # Now, since one list will be None, point nextNode to the rest of the other list
    nextNode.next = l1 if l1 else l2

    return preHead.next


def main():
    print(merge())
    print(merge())
    print(merge())

if __name__ == "__main__":
    main()
