import re

def check_password_strength(pw):
    if len(pw) < 8:
        return "Weak"
    if not re.search(r'[A-Z]', pw):
        return "Weak"
    if not re.search(r'[a-z]', pw):
        return "Weak"
    if not re.search(r'[0-9]', pw):
        return "Weak"
    if not re.search(r'[\W_]', pw):
        return "Weak"
    return "Strong"

pw = input()
print(check_password_strength(pw))
