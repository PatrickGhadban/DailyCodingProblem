'''
* Difficulty: Medium
* Asked by: Microsoft
* Problem: Given a number in the form of a list of digits, return all possible permutations.
For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].


Time Taken:
RunTime:
Space Complexity:

Description:
'''

def permutations(lst):
    if len(lst) == 0:
        return
    if len(lst) == 1:
        return lst

    result = []

    for i in range(len([lst])):
        char = lst[i]
        permus = lst[:i] + lst[i+1:]
        for perm in permutations([permus]):
            temp = [char] + [perm]
            result.append(temp)

    return result


def main():
    for perm in permutations([1,2,3]):
        print (perm)

    # for perm in permutations([1,2,3,4]):
    #     print (perm)

if __name__ == "__main__":
    main()
