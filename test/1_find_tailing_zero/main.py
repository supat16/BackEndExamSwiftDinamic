"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


# class Solution:

#     def find_tailing_zeroes(self, number: int) -> int | str:
#         pass

class Solution:
    def find_tailing_zeroes(self, number: int) -> int or str:
        if number < 0:
            return "number can not be negative"
        
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            result = 1
            for i in range(2, num + 1):
                result *= i
            return result
        
        user_factorial = factorial(number)
        
        count_zeros = 0
        while user_factorial % 10 == 0:
            count_zeros += 1
            user_factorial //= 10
        
        return count_zeros
    
sol = Solution()
user_input = int(input("Enter a number: "))
print(sol.find_tailing_zeroes(user_input))