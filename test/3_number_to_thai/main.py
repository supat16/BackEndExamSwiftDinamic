"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""

def number_to_thai_text(number):
    if number < 0:
        return "number can not less than 0"
    
    if number == 0:
        return "ศูนย์"

    digits = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    positions = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

    num_text = ""
    position_index = 0
    while number > 0:
        digit = number % 10
        if digit > 0 or (digit == 0 and (position_index == 0 or (position_index == 6 and number >= 10))):
            if digit == 1 and position_index == 1 and (number % 100 == 11):
                num_text = positions[position_index] + num_text
            else:
                num_text = digits[digit] + positions[position_index] + num_text
        number //= 10
        position_index += 1

    return num_text

input_number = int(input("Enter number: "))
output_text = number_to_thai_text(input_number)
print(f"Output: {output_text}")
