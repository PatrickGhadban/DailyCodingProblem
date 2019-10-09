'''
* Difficulty: Easy
* Asked by: FAANG, Cisco (much less than other companies)
* Problem: Given a sorted array nums, remove the duplicates in-place such that each element appear only once
and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

EXAMPLE:
Given nums = [1,1,2]
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

Time Taken: < 10mins
RunTime: O(N)
Space Complexity: O(1)

Description: I don't think it needs it
'''

def removeDupicates(nums):
    if len(nums) == 0:
        return 0

    compare = nums[0]
    i = 1
    while i < len(nums):
        if compare == nums[i]:
            del nums[i]
        else:
            compare = nums[i]
            i += 1

    return len(nums)


def main():
    print(removeDupicates([1,1,2]))
    print(removeDupicates([1,1,1,1,2,2,2,3,3,3,4]))

if __name__ == "__main__":
    main()
