import re

    # check for password strength characters
length_regex = r'.{8,}'
uppercase_regex = r'[A-Z]'
lowercase_regex = r'[a-z]'
digit_regex = r'\d'
special_char_regex = r'[!@#$%^&*()-+=.]'
password = input("Enter your password: ")

if not re.search(length_regex, password):
    print ("Password should be at least 8 characters long.")

if not re.search(uppercase_regex, password):
    print ("Password should contain at least one uppercase letter.")

if not re.search(lowercase_regex, password):
    print ("Password should contain at least one lowercase letter.")

if not re.search(digit_regex, password):
    print ("Password should contain at least one digit.")

if not re.search(special_char_regex, password):
    print("Password should contain at least one special character.")
print("Password is strong!")

strength_result = password
print(strength_result)
