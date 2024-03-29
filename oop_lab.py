# -*- coding: utf-8 -*-
"""oop lab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_U0aaGPivMMLjGnKRW_STECRyKT6x4Wt
"""

def find_largest_element(input_list):
    if not input_list:
        return "The list is empty."

    largest_element = input_list[0]

    for element in input_list:
        if element > largest_element:
            largest_element = element

    return largest_element

# Example usage:
my_list = [12, 45, 78, 34, 56, 89, 23]
result = find_largest_element(my_list)

print(f"The largest element in the list is: {result}")

import math

def hexagon_area(side_length):
    area = (3 * math.sqrt(3) / 2) * (side_length ** 2)
    return area

# Example usage:
side_length = 5
area_result = hexagon_area(side_length)

print(f"The area of a regular hexagon with side length {side_length} is: {area_result}")

import re

def is_valid_email(email):
    # Define the email validation pattern
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,}$'

    # Use regular expression to check if the email matches the pattern
    return bool(re.match(pattern, email))

# Example usage:
email_address = "example@email.com"
result = is_valid_email(email_address)

print(f"Is {email_address} a valid email address? {result}")

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

# Example usage:
text_to_encrypt = "Hello, World!"
shift_value = 3

encrypted_text = encrypt(text_to_encrypt, shift_value)
print(f"Encrypted text: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, shift_value)
print(f"Decrypted text: {decrypted_text}")

def get_palindromes(input_string):
    words = input_string.split()
    palindromes = [word for word in words if word == word[::-1]]
    return palindromes

# Example usage:
input_string = "level radar python madam racecar"
result = get_palindromes(input_string)

print(f"Palindromes in the string: {result}")