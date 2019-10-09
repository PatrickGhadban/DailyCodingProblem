"""
Difficulty: Easy
Comapanies: Basically all of them - notable for me: Amazon, Wayfair, Oracle
Description: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

EX: Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

Time Taken: 30mins
Run-time: O(n)
Space Complexity: O(n)
Solution: Convert the list to a hash table { value : index } because a map has a constant look up. While converting,
find the difference, check if it's in the hash table. If so, return the index and the value of the hash.

Personal Note / Goal: This shouldn't take more than 10mins
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#       Base Case
        if len(nums) == 0:
            return []

#       Convert list of nums to hash of nums { value : indices }
#       Find the difference between nums and target and search in hash
        indices = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in indices:
                if i != indices[difference]:
                    return [i, indices[difference]]
            indices[nums[i]] = i
        return []


def main():
    obj = Solution()
    print (obj.twoSum([2, 7, 11, 15], 9))
    print (obj.twoSum([-1, -2, -3, -4, -5], -8))
    print (obj.twoSum([3, 2, 4], 6))
    print (obj.twoSum([2, 1, 9, 5, 3], 8))
    print (obj.twoSum([2, 1, 9, 4, 4], 8))


if __name__ == "__main__":
    main()
