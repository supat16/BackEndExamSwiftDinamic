"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""

class Solution:
    
    def number_to_roman(self, number: int) -> str:
        if number <= 0:
            return "number can not be less than 0"
        
        roman_numerals = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }
        
        result = ""
        
        for value, roman in roman_numerals.items():
            while number >= value:
                result += roman
                number -= value
        
        return result

solution = Solution()

input_number = int(input("Enter a number to convert to Roman numeral: "))

output_roman = solution.number_to_roman(input_number)
print(f"Input: {input_number}, Output: {output_roman}")
