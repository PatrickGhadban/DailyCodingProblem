'''
* Difficulty: Medium
* Asked by: Facebook
* Problem: Write a function that rotates a list by k elements.
For example, [1, 2, 3, 4, 5, 6] rotated by two becomes
             [3, 4, 5, 6, 1, 2].
Try solving this without creating a copy of the list.
How many swap or move operations do you need?


Time Taken: < 10mins
RunTime: O(N*K)
Space Complexity: O(1)

Description:
Sol #1 - Swap through the list for k.
Sol #2 (Couldn't get working) - Find the gcd of len of the list and number of rotations. Then separate the list into sets the size of the gcd
and swap
'''

def sol1(lst, k):
    for x in k:
        for i in range(len(lst) - 1):
            lst[i], lst[i+1] = lst[i+1], lst[i]


def g_c_d(a, b):
    if b == 0:
        return a;
    else:
        return g_c_d(b, a % b)

def rotate(lst, k):
    n = len(lst)
    if k == 0 or n == 0:
        return
    if k == n:
        return lst

    gcd = g_c_d(n, k)
    for i in range(0, gcd):
        j = i
        while True:
            index = j + gcd
            if index >= n:
                break
            lst[j], lst[index] = lst[index], lst[j]
            j = index

    return lst

def main():
    print (rotate([1,2,3,4,5,6], 1))
    print (rotate([1,2,3,4,5,6], 2))
    print (rotate([1,2,3,4,5,6], 3))
    print (rotate([1,2,3,4,5,6], 4))
    print (rotate([1,2,3,4,5,6], 5))
    print (rotate([1,2,3,4,5,6], 6))

if __name__ == "__main__":
    main()
