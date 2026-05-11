import regex as re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

email = input("Enter an email address: ")
if validate_email(email):
    print(email,"is a valid email address.")
else:
    print(email, "is an invalid email address.")