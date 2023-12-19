import re
import os

def find_txt_file_in_current_directory():
    for file in os.listdir():
        if file.endswith(".txt"):
            return file
    return None

def convert_spelled_digit_to_number(spelled_digit):
    mapping = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "oneight": 18, "eightwo": 82, "twone": 21, "sevenine": 79, "nineight": 98, "eighthree": 83, "threeight": 38, "fiveight": 58, "oneightwo": 182, "eightwone": 821, "twoneight": 218}
    return mapping.get(spelled_digit.lower(), None)

def extract_digits_from_line(line):
    digits = re.findall(r'(?:oneightwo|eightwone|twoneight|oneight|eightwo|twone|sevenine|nineight|eighthree|threeight|fiveight|one|two|three|four|five|six|seven|eight|nine)|\d', line.lower())
    # print(f"digits: {digits}")
    digits = [str(convert_spelled_digit_to_number(digit) if digit.isalpha() else digit) for digit in digits]
    return digits

def process_lines(lines):
    total_sum = 0
    lNum = 1
    for line in lines:
        digits = extract_digits_from_line(line)
        if digits:
            concatenated_digits = ''.join(digits)
            first_digit = concatenated_digits[0]
            last_digit = concatenated_digits[-1]
            two_digit_number = int(first_digit + last_digit)
            total_sum += two_digit_number
            print(f"Line {lNum}: {line.strip()}, Two-digit number: {two_digit_number}, digits: {digits}")
            lNum += 1

    print(f"Total sum: {total_sum}")

txt_file = find_txt_file_in_current_directory()

if txt_file:
    with open(txt_file, 'r') as file:
        lines = file.readlines()
        process_lines(lines)
else:
    print("No .txt file found in the current directory.")
