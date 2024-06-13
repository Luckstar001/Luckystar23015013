import re
email = input("Enter your email address: ")
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(email_regex, email):
     print("valid email")
else:
    print('not matched to regular email')
