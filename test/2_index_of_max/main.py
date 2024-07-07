"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""

from typing import Union

class Solution:

    def find_max_index(self, numbers: list) -> Union[int, str]:
        if not numbers:
            return "list cannot be blank"

        max_num = max(numbers)
        max_index = numbers.index(max_num)
        return max_index

sol = Solution()

input_list = []
while len(input_list) < 7:
    try:
        num = int(input(f"Enter number {len(input_list) + 1} (or press Enter to finish): "))
        input_list.append(num)
    except ValueError:
        break

if input_list:
    print("Input list:", input_list)
    print("Index of maximum number:", sol.find_max_index(input_list))
else:
    print("List cannot be blank")