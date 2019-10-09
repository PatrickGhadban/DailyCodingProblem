'''
* Difficulty: Easy
* Asked by: FAANG
* Problem: The count-and-say sequence is the sequence of integers with the first five terms as following:
EXAMPLES:
    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

Time Taken: 30mins
RunTime: O(n^2) - best RunTime
Space Complexity: O(1)

Description:
    1.) Iterate the number of times given in n.
    2.) Get the first char, count the number of times it occurs and set a temp string equal to the concatenation of the count & char
    3.) Update the answer and return
'''

def solution(n):
  if not n:
      return 0

  if n == 1:
      return "1"

  answer = "1"
  i = 1
  while i < n:
      update = ""
      j = 0
      while j < len(answer):
          char = answer[j]
          count = 1
          j += 1
          while j < len(answer) and char == answer[j]:
              count += 1
              j += 1
          update += str(count) + char

      i += 1
      answer = update

  return answer


def main():
    print(solution())
    print(solution())
    print(solution())

if __name__ == "__main__":
    main()
